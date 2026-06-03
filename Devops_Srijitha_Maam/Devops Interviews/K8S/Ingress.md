# 20. What is Ingress in Kubernetes?

## Simple Interview Answer

In Kubernetes, **Ingress** is an API object used to manage external access to applications running inside the cluster.

Ingress provides:

* HTTP/HTTPS routing
* Domain-based access
* Path-based routing
* SSL termination
* Load balancing

Instead of exposing every application using separate LoadBalancer services, Ingress provides a single entry point.

---

# Why Ingress is Needed?

Suppose a Kubernetes cluster has:

* Frontend application
* Backend API
* Admin dashboard

Without Ingress:

* Separate LoadBalancer needed for each service
* Higher cloud cost
* Complex management

Ingress solves this problem using one centralized routing system.

---

# Without Ingress

```text id="jlwm9d"
Internet
   ↓
LoadBalancer → Frontend
LoadBalancer → Backend
LoadBalancer → Admin
```

Multiple external load balancers are required.

---

# With Ingress

```text id="jlwmu7"
Internet
    ↓
Ingress
 ├── / → Frontend
 ├── /api → Backend
 └── /admin → Admin
```

Single entry point handles all routing.

---

# What Does Ingress Do?

Ingress manages:

* External traffic routing
* URL-based routing
* Domain-based routing
* SSL certificates
* Reverse proxy functionality

---

# Main Components of Ingress

| Component          | Purpose                |
| ------------------ | ---------------------- |
| Ingress Resource   | Routing rules          |
| Ingress Controller | Implements rules       |
| Service            | Routes traffic to pods |

---

# Important Point

Ingress itself does not work alone.

It requires:

# Ingress Controller

Popular controllers:

* NGINX Ingress Controller
* Traefik
* HAProxy Ingress

---

# Ingress Workflow

```text id="jlwmb7"
User Request
      ↓
Ingress Controller
      ↓
Ingress Rules
      ↓
Kubernetes Service
      ↓
Pods
```

---

# Types of Routing in Ingress

---

# 1. Path-Based Routing

Routes traffic based on URL path.

Example:

| URL      | Service     |
| -------- | ----------- |
| `/`      | Frontend    |
| `/api`   | Backend     |
| `/admin` | Admin Panel |

---

# 2. Host-Based Routing

Routes traffic based on domain name.

Example:

| Domain          | Service  |
| --------------- | -------- |
| app.example.com | Frontend |
| api.example.com | Backend  |

---

# Sample Ingress YAML File

## ingress.yaml

```yaml id="jlwmh9"
apiVersion: networking.k8s.io/v1
kind: Ingress

metadata:
  name: my-ingress

spec:
  rules:
  - host: myapp.com

    http:
      paths:
      - path: /
        pathType: Prefix

        backend:
          service:
            name: frontend-service

            port:
              number: 80
```

---

# Explanation of Ingress YAML

---

# 1. apiVersion

```yaml id="jlwmd1"
apiVersion: networking.k8s.io/v1
```

Defines Kubernetes networking API version.

---

# 2. kind

```yaml id="jlwm0k"
kind: Ingress
```

Defines resource type.

---

# 3. host

```yaml id="jlwm2v"
host: myapp.com
```

Defines domain name.

---

# 4. path

```yaml id="jlwm7a"
path: /
```

Defines request path.

---

# 5. backend service

```yaml id="jlwmbq"
service:
  name: frontend-service
```

Routes traffic to Kubernetes service.

---

# How to Apply Ingress

---

# Step 1: Install Ingress Controller

Example:

* NGINX Ingress Controller

---

# Step 2: Apply YAML File

```bash id="jlwmv8"
kubectl apply -f ingress.yaml
```

---

# Step 3: Check Ingress

```bash id="jlwmdx"
kubectl get ingress
```

---

# Advantages of Ingress

| Advantage           | Explanation                 |
| ------------------- | --------------------------- |
| Single Entry Point  | Simplifies access           |
| Cost Effective      | Fewer load balancers        |
| SSL Support         | HTTPS management            |
| Centralized Routing | Easier management           |
| Path-Based Routing  | Multiple apps on one domain |

---

# Ingress vs LoadBalancer

| Ingress              | LoadBalancer       |
| -------------------- | ------------------ |
| Layer 7 (HTTP/HTTPS) | Layer 4 (TCP/UDP)  |
| Smart routing        | Basic exposure     |
| One entry point      | One LB per service |
| Cost efficient       | More expensive     |

---

# Real-Time Example

Suppose an e-commerce platform has:

* Frontend
* Payment API
* Admin panel

Ingress routes traffic like:

| URL            | Destination |
| -------------- | ----------- |
| shop.com       | Frontend    |
| shop.com/api   | Backend API |
| shop.com/admin | Admin Panel |

---

# SSL/TLS in Ingress

Ingress supports HTTPS using TLS certificates.

Example:

```yaml id="jlwmi4"
tls:
- hosts:
  - myapp.com
```

---

# Common Ingress Controllers

| Controller    | Description      |
| ------------- | ---------------- |
| NGINX Ingress | Most popular     |
| Traefik       | Cloud-native     |
| HAProxy       | High-performance |

---

# Important Interview Follow-Up Questions

---

## What is Ingress Controller?

A component that implements Ingress rules.

---

## Does Ingress Work Without Controller?

No.

Ingress requires a controller.

---

## Why Ingress is Better Than Multiple LoadBalancers?

Because:

* Lower cost
* Centralized management
* Advanced routing

---

# Ingress Architecture Diagram

```text id="jlwm2x"
Internet
    ↓
Ingress Controller
    ↓
Ingress Rules
    ↓
Services
    ↓
Pods
```

---

# Production Example

Companies use Ingress for:

* Microservices routing
* HTTPS termination
* API gateways

Very common in Kubernetes production environments.

---

# Short Interview Version (2-Minute Answer)

“Ingress is a Kubernetes API object used to manage external access to services inside a cluster. It provides HTTP and HTTPS routing, SSL termination, and path-based or domain-based routing.

Ingress acts as a centralized entry point for applications and requires an Ingress Controller like NGINX Ingress Controller to function. It helps reduce cost and simplifies routing management in Kubernetes environments.”
