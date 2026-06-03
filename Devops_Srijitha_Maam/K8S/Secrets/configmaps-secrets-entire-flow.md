```text
Internet
   ↓
Ingress / LoadBalancer
   → Entry point for external traffic
   → Receives requests on 80/443

   ↓
Frontend Service (ClusterIP)
   → Exposes frontend Pods internally
   → port: 80
   → targetPort: 80

   ↓
Frontend Pods
   → Running React/Angular/Vue/Nginx
   → containerPort: 80
   → Reads configuration from ConfigMap
   → Reads sensitive data from Secret

      ┌─────────────────────┐
      │ Frontend ConfigMap  │
      │ API_URL             │
      │ APP_NAME            │
      │ ENVIRONMENT         │
      └──────────┬──────────┘
                 │
                 ▼

      ┌─────────────────────┐
      │ Frontend Secret     │
      │ API_KEY             │
      │ TOKEN               │
      │ LICENSE_KEY         │
      └──────────┬──────────┘
                 │
                 ▼

   ↓
Backend Service (ClusterIP)
   → Internal service for backend access
   → port: 5000
   → targetPort: 5000

   ↓
Backend Pods
   → Running Flask/FastAPI/Django/Node.js
   → containerPort: 5000
   → Reads configuration from ConfigMap
   → Reads sensitive data from Secret

      ┌─────────────────────┐
      │ Backend ConfigMap   │
      │ DB_HOST             │
      │ DB_PORT             │
      │ LOG_LEVEL           │
      └──────────┬──────────┘
                 │
                 ▼

      ┌─────────────────────┐
      │ Backend Secret      │
      │ DB_USER             │
      │ DB_PASSWORD         │
      │ JWT_SECRET          │
      └──────────┬──────────┘
                 │
                 ▼

   ↓
Database Service (ClusterIP)
   → Internal database access
   → port: 5432
   → targetPort: 5432

   ↓
Database Pod / RDS
   → PostgreSQL/MySQL
```

### Request Flow

```text
User Browser
     ↓
Ingress / LoadBalancer
     ↓
Frontend Service
     ↓
Frontend Pod

     Frontend Pod loads:
     ├─ ConfigMap → API_URL=http://backend-service:5000
     └─ Secret → API_KEY=*****

     ↓
Backend Service
     ↓
Backend Pod

     Backend Pod loads:
     ├─ ConfigMap → DB_HOST, DB_PORT
     └─ Secret → DB_USER, DB_PASSWORD

     ↓
Database
     ↓
Response
     ↑
Backend Pod
     ↑
Frontend Pod
     ↑
User Browser
```

### What ConfigMap and Secret Do

```text
ConfigMap
   ↓
Non-sensitive configuration
   Examples:
   - API_URL
   - DB_HOST
   - ENVIRONMENT
   - LOG_LEVEL

Secret
   ↓
Sensitive configuration
   Examples:
   - Passwords
   - API Keys
   - Tokens
   - JWT Secrets
```

### Complete Production Flow

```text
Internet
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
      ↑
      ├── ConfigMap
      └── Secret
   ↓
Backend Service (ClusterIP)
   ↓
Backend Pods
      ↑
      ├── ConfigMap
      └── Secret
   ↓
Database Service (ClusterIP)
   ↓
Database Pod / RDS
```

A good mental model is:

```text
ConfigMap + Secret
          ↓
      Pod Starts
          ↓
Application reads values
          ↓
Application serves requests
```

ConfigMaps and Secrets are **not in the request path**. They are mounted into Pods (as environment variables or files) and are used by the application while it runs.
