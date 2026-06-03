
Internet
      ↓
Ingress
      ↓
Frontend Service
      ↓
Frontend Pods
      ↓
Backend Service
      ↓
Backend Pods
      ↓
Database Service
      ↓
Database Pods


# Communication Flow Between Frontend Pod and Backend Pods

In Frontend Pod application , we write backend API calls like:

```javascript
fetch("http://backend-service") => http://backend-service:80
```
```python
requests.get("http://backend-service") => http://backend-service:80
```python
<form action="http://backend-service" > => http://backend-service:80
</form>
```
```javascript
axios.get("http://backend-service") -> http://backend-service:80

Check This files:- backend-clusterip.yaml
`backend-service` name of service for the Backend Pods ,Exposed in port 80 and Target the Backend Pods Containers port 5678

---------         -----------         -----------          -------------


```bash

Frontend Pod Request >`http://backend-service:80` (Send a Request To Backend Service) 
      │
      ▼
DNS Resolution converts `backend-service to 10.96.10.5`
      │
      ▼
backend-service:80(Recieved a Request From Frontend) (backend-service Expose itself at 80)
(10.96.10.5:80)
      │
      ▼
backend-service Knows The Backend Pods Through Selectors And Labels In ymal file
backend-service Searced The Backend Pods For Fowarding The Request 
backend-service Forwarded Traffic to Backend Pods:5678 
      │
      ▼
Backend Pods:5678      
(10.244.0.5:5678)
      │
      ▼
Container App Responds
      │
      ▼
Hello From Backend API

```


# 👉👉First Step 1 :- Accesing App in Pods 👈👈
## If you access container:

This file :- backend-deployment.yaml

```ymal
  ports:
  - containerPort: 5678
```

Your backend container application is running on:

```text id="bdj0bm"
Port 5678
```



```text id="g87d0w"
http://pod-ip:5678
```

Response:

```text id="nmr1fi"
Hello From Backend API
```

---

## What Does containerPort Mean?

```yaml id="ah5sj4"
containerPort: 5678
```

Means:

```text id="8v9hzd"
Application inside container listens on port 5678
```

This does NOT expose application externally.

It only tells Kubernetes:

> “My application runs on port 5678”

---

## Internal Pod Situation

Suppose Pod IP:

```text id="7l4m8w"
10.244.0.5
```

Application accessible at:

```text id="ljuxu0"
10.244.0.5:5678
```


# 👉👉 Second Step  :- Accesing App By backend-service  👈👈


### backend-service.yaml

```yaml id="gzjlwm"
ports:
- port: 80
  targetPort: 5678
```


### What is port?

```yaml id="q9g74g"
port: 80
```

Means:

backend-Service exposes itself on:

```text id="24qqbo"
backend-service:80
```

Clients talk to Service using port 80.

But inside Kubernetes, we want backend-services to access it using:

```text id="5olc1g"
Port 80
```

---

### What is targetPort?

```yaml id="xfp16n"
targetPort: 5678
```

Means:

Forward traffic to Pod on:

```text id="mfjlwm"
PodIP:5678
```

## 👉👉 Real Internal Example 👈👈

Suppose:

### Service IP

```text id="chjlwm"
10.96.10.5
```

### Backend Pod IP

```text id="crqqtx"
10.244.0.5
```

---

### Step-by-Step Flow

Frontend calls:

```text id="bjlwm6"
http://backend-service:80
```

DNS converts:

```text id="8n9syq"
backend-service
      ↓
10.96.10.5
```

Service receives traffic:

```text id="9jjlwm"
10.96.10.5:80
```

Then forwards to:

```text id="9ijvdq"
10.244.0.5:5678
```

Backend container responds:

```text id="jlwm6v"
Hello From Backend API
```

backend-service IP :- 10.96.10.5

Backend Pod IP :- 10.244.0.5

```bash

Frontend Pod Request >`http://backend-service:80` (Send a Request To Backend Service) 
      │
      ▼
DNS Resolution converts `backend-service to 10.96.10.5`
      │
      ▼
backend-service:80(Recieved a Request From Frontend) (backend-service Expose itself at 80)
(10.96.10.5:80)
      │
      ▼
backend-service Knows The Backend Pods Through Selectors And Labels In ymal file
backend-service Searced The Backend Pods For Fowarding The Request 
backend-service Forwarded Traffic to Backend Pods:5678 
      │
      ▼
Backend Pods:5678      
(10.244.0.5:5678)
      │
      ▼
Container App Responds
      │
      ▼
Hello From Backend API

```

