```bash
*****
Applications Of Frontend Pods Internally Calling the backend-service By API call that we mentions their 
*****
```
In frontend application code, we write backend API calls like:

```javascript
fetch("http://backend-service/api")
```

or

```python
requests.get("http://backend-service/api")
```

```python
<form action="http://backend-service/api" method=GET>

</form>
```
or

```javascript
axios.get("http://backend-service/api")
```

Kubernetes automatically connects frontend Pods to backend Pods using:

* Service DNS
* ClusterIP
* kube-proxy
* label selectors
* Pod networking
In frontend application code, we write backend API calls like:

```text id="nq7q0n"
http://backend-service
```

or

```text id="4o5rf9"
http://backend-service/api
```

Kubernetes automatically routes this to backend Pods.

---

# REAL PROJECT FLOW

```text id="yivh5h"
Frontend App
     ↓
Backend Service DNS
     ↓
Backend Service
     ↓
Backend Pods
```

---

# Example with Flask Backend

Suppose Flask backend runs:

```python id="2v7m7z"
@app.route("/users")
def users():
    return {"name": "Roshan"}
```

Frontend calls:

```javascript id="70rv5m"
fetch("http://backend-service/users")
```

---

# Example with FastAPI Backend

Backend:

```python id="85bknu"
@app.get("/products")
def products():
    return {"product": "Laptop"}
```

Frontend:

```javascript id="e7m6j5"
fetch("http://backend-service/products")
```

---

# Example with NodeJS Backend

Backend:

```javascript id="o9iwbo"
app.get("/api", (req, res) => {
  res.send("Hello from NodeJS");
});
```

Frontend:

```javascript id="g9zvks"
fetch("http://backend-service/api")
```

---

# VERY IMPORTANT UNDERSTANDING

Frontend does NOT call:

❌ Pod IP
❌ NodePort
❌ containerPort directly

Frontend calls ONLY:

```text id="aslv7r"
Service Name
```

because Kubernetes DNS resolves it automatically.

---

# Kubernetes Internal DNS

Your backend Service:

```yaml id="mjlwm6"
metadata:
  name: backend-service
```

automatically becomes:

```text id="5jlwm7"
backend-service
```

usable inside cluster.

---

# COMPLETE INTERNAL FLOW

```text id="3jlwm8"
Frontend App Code
       │
       ▼
http://backend-service/api
       │
       ▼
CoreDNS resolves name
       │
       ▼
ClusterIP
       │
       ▼
Backend Pods
```

---

# Real React Example

Suppose React frontend.

---

# React Frontend Code

```javascript id="1jlwm9"
import { useEffect } from "react";

function App() {

  useEffect(() => {

    fetch("http://backend-service/api")
      .then(res => res.text())
      .then(data => console.log(data));

  }, []);

  return <h1>Frontend App</h1>;
}

export default App;
```

---

# How Kubernetes Handles This

Frontend Pod sends request:

```text id="zjlw10"
backend-service
```

Kubernetes:

* resolves DNS
* finds ClusterIP
* forwards to backend Pod
* load balances traffic

Automatically.

---

# IMPORTANT REAL PROJECT THINKING

# Inside Kubernetes Cluster

Applications communicate using:

```text id="xjlw11"
Service Names
```

NOT:

* localhost
* public IP
* Pod IP

---

# Real Production Example

```text id="vjlw12"
frontend-service
auth-service
payment-service
order-service
user-service
redis-service
mongo-service
```

All microservices communicate using Service DNS names.

---

# MOST IMPORTANT MINDSET

Think like this:

```text id="tjlw13"
Kubernetes Service
   =
Internal DNS + Load Balancer
```

---

# Real Backend URL Patterns

| Backend Type | Example URL                                                  |
| ------------ | ------------------------------------------------------------ |
| Flask        | [http://backend-service/users](http://backend-service/users) |
| FastAPI      | [http://backend-service/docs](http://backend-service/docs)   |
| NodeJS       | [http://backend-service/api](http://backend-service/api)     |
| Django       | [http://backend-service/admin](http://backend-service/admin) |

---

# FINAL UNDERSTANDING

YES.

