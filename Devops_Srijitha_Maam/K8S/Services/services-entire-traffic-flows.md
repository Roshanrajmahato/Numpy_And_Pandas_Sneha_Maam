
```bash
Internet
   ↓
Ingress / LoadBalancer
   → Entry point for external users
   → Type:
       - Ingress (HTTP/HTTPS routing)
       - LoadBalancer Service (Cloud LB)
   → Receives traffic on:
       - 80 (HTTP)
       - 443 (HTTPS)
   → Send traffic on:
       - port: 80 

   ↓
Frontend Service
   → Kubernetes Service exposing frontend Pods
   → Usually Type: ClusterIP
   → port: 80
   → targetPort: 80

   ↓
Frontend Pods
   → Running frontend application (React, Angular, Vue, Nginx)
   → containerPort: 80

frontend app code calls:
http://backend-service:5000

   ↓
Backend Service
   → Internal Service used by frontend to reach backend
   → Usually Type: ClusterIP
   → port: 5000
   → targetPort: 5000

   ↓
Backend Pods
   → Running backend application (Flask, FastAPI, Node.js, Django)
   → containerPort: 5000

   ↓
Application
   → Business logic executes here
   → Processes requests and returns responses
```

### Example YAML Mapping

```bash
Internet
   ↓
Ingress
   ↓
frontend-service
    port: 80
    targetPort: 80
   ↓
frontend-pod
    containerPort: 80

frontend code calls:
http://backend-service:5000

   ↓
backend-service
    port: 5000
    targetPort: 5000
   ↓
backend-pod
    containerPort: 5000
   ↓
Flask/FastAPI Application
```

### Real Production Architecture

```text
User Browser
     ↓
DNS (myapp.com)
     ↓
Cloud Load Balancer
     ↓
Ingress Controller
     ↓
Frontend Service (ClusterIP)
     ↓
Frontend Pods
     ↓
Backend Service (ClusterIP)
     ↓
Backend Pods
     ↓
Database Service (ClusterIP)
     ↓
Database Pods / RDS
```

**Rule to remember:**

```text
External User
    ↓
Ingress / LoadBalancer
    ↓
Service Port
    ↓
TargetPort
    ↓
ContainerPort
    ↓
Application
```

Where:

```text
port         = Service port
targetPort   = Pod port
containerPort= Application listening port
```

LoadBalancer
     ↓
Service Port      → Port exposed by the Kubernetes Service  (port: 80)
     ↓
TargetPort        → Port on the Pod where traffic is forwarded (targetPort: 8080)
     ↓
ContainerPort     → Port on which the container/application listens (containerPort: 8080)
     ↓
Application       → Your actual application process (Nginx, Flask, Node.js, etc.)
