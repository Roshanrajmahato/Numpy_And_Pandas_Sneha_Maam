Create
Nginx-Deployment.yaml
Nginx-Loadbalancer-Service.yaml



Commands Execution
kubectl apply -f Nginx-Deployment.yaml


➡ Deploys Pods

kubectl apply -f Nginx-Loadbalancer-Service.yaml


➡ Creates Service

kubectl get deployments


➡ Check deployment status

kubectl get pods -o wide


➡ View Pod IPs & nodes

kubectl get svc


➡ View Service type & External IP


# Complete Deep Understanding of Frontend Deployment + LoadBalancer Service

You want to understand:

```yaml
frontend-deployment.yaml
frontend-service.yaml
```

especially:

```yaml
ports:
  - port: 80
    targetPort: 80
```

and:

* how frontend Pods work
* how LoadBalancer works
* how traffic flows internally
* how Service connects Pods
* how Kubernetes networking works internally

This is one of the MOST IMPORTANT Kubernetes concepts.

---

# YOUR FRONTEND DEPLOYMENT

```yaml id="ghr4o2"
apiVersion: apps/v1
kind: Deployment

metadata:
  name: frontend

spec:
  replicas: 2

  selector:
    matchLabels:
      app: frontend

  template:
    metadata:
      labels:
        app: frontend

    spec:
      containers:
      - name: frontend

        image: nginx:latest

        ports:
        - containerPort: 80
```

---

# STEP 1 — What Deployment Does

Deployment is an:

```text id="zjlwm1"
Application Manager
```

Its job:

* create Pods
* maintain Pods
* restart failed Pods
* scale Pods
* update Pods

---

# STEP 2 — Replicas

```yaml id="yjlwm2"
replicas: 2
```

Means:

```text id="xjlwm3"
Run 2 frontend Pods
```

Kubernetes creates:

```text id="wjlwm4"
frontend-pod-1
frontend-pod-2
```

---

# STEP 3 — Labels

```yaml id="vjlwm5"
labels:
  app: frontend
```

VERY IMPORTANT.

Each Pod gets:

```text id="ujlwm6"
app=frontend
```

This is Pod identity.

---

# STEP 4 — Container

```yaml id="tjlwm7"
image: nginx:latest
```

Inside Pod, Kubernetes runs:

```text id="sjlwm8"
NGINX Web Server
```

---

# STEP 5 — containerPort

```yaml id="rjlwm9"
containerPort: 80
```

Means:

```text id="qjlw10"
NGINX listens internally on port 80
```

---

# IMPORTANT UNDERSTANDING

Inside Pod:

```text id="pjlw11"
NGINX App
     ↓
Listening on port 80
```

---

# POD NETWORKING

Each Pod gets unique IP.

Example:

```text id="ojlw12"
frontend-pod-1 → 10.244.1.3
frontend-pod-2 → 10.244.1.4
```

NGINX accessible at:

```text id="njlw13"
10.244.1.3:80
10.244.1.4:80
```

BUT:

❌ Internet cannot access these Pod IPs directly.

Why?

Because Pod IPs are internal cluster network.

---

# Therefore We Need SERVICE

---

# YOUR FRONTEND SERVICE

```yaml id="mjlw14"
apiVersion: v1
kind: Service

metadata:
  name: frontend-service

spec:
  type: LoadBalancer

  selector:
    app: frontend

  ports:
    - port: 80
      targetPort: 80
```

---

# STEP 1 — What Service Does

Service is:

```text id="ljlw15"
Network Manager
```

Its job:

* stable networking
* stable DNS
* load balancing
* traffic forwarding

---

# STEP 2 — selector

```yaml id="kjlw16"
selector:
  app: frontend
```

Service searches:

```text id="jjlw17"
Find Pods with label app=frontend
```

It finds:

```text id="ijjw18"
frontend-pod-1
frontend-pod-2
```

Now Service connects to these Pods.

---

# MOST IMPORTANT CONCEPT

# Labels + Selectors = Connection

```text id="hjlw19"
Pods expose labels

Services use selectors
```

---

# STEP 3 — LoadBalancer Type

```yaml id="gjlw20"
type: LoadBalancer
```

This is cloud integration feature.

---

# What Kubernetes Does Internally

Kubernetes asks cloud provider:

```text id="fjlw21"
Create External Load Balancer
```

If AWS:

* ELB
* ALB
* NLB

If GCP:

* Cloud Load Balancer

---

# Traffic Flow

```text id="ejlw22"
Internet User
      ↓
Cloud Load Balancer
      ↓
frontend-service
      ↓
frontend Pods
```

---

# MOST IMPORTANT PART

# ports Section

```yaml
ports:
  - port: 80
    targetPort: 80
```

Let's deeply understand this.

---

# What is port?

```yaml id="djlw23"
port: 80
```

Means:

Service exposes itself on:

```text id="cjlw24"
frontend-service:80
```

Clients communicate with Service using port 80.

---

# What is targetPort?

```yaml id="bjlw25"
targetPort: 80
```

Means:

Forward traffic to Pod on:

```text id="ajlw26"
PodIP:80
```

---

# FULL INTERNAL FLOW

Suppose:

## Service IP

```text id="9jlw27"
10.96.20.5
```

## Pod IPs

```text id="8jlw28"
10.244.1.3
10.244.1.4
```

---

# User Request Journey

## Step 1

Browser opens:

```text id="7jlw29"
http://LoadBalancer-IP
```

---

# Step 2

Cloud Load Balancer receives request.

---

# Step 3

LoadBalancer forwards request to:

```text id="6jlw30"
frontend-service:80
```

---

# Step 4

Service checks endpoints:

```text id="5jlw31"
frontend-pod-1:80
frontend-pod-2:80
```

---

# Step 5

kube-proxy forwards traffic.

---

# Step 6

NGINX Pod receives request.

---

# Step 7

NGINX sends webpage response.

---

# VISUAL FLOW

```text id="4jlw32"
Browser
   │
   ▼
Cloud Load Balancer
   │
   ▼
frontend-service:80
   │
   ▼
Service forwards traffic
   │
   ├──────────────┐
   ▼              ▼
Pod1:80       Pod2:80
```

---

# Why Both Ports Are 80?

Because:

NGINX internally runs on:

```text id="3jlw33"
80
```

and Service also exposes:

```text id="2jlw34"
80
```

So:

```yaml
port: 80
targetPort: 80
```

---

# Real Project Examples

# Example 1 — React App

React app runs on:

```text id="1jlw35"
3000
```

Service:

```yaml id="zjlw36"
port: 80
targetPort: 3000
```

---

# Example 2 — Flask App

Flask runs on:

```text id="xjlw37"
5000
```

Service:

```yaml id="wjlw38"
port: 80
targetPort: 5000
```

---

# Example 3 — NodeJS App

NodeJS runs on:

```text id="vjlw39"
3000
```

Service:

```yaml id="ujlw40"
port: 80
targetPort: 3000
```

---

# Why Service Port Usually 80?

Because:

* standard HTTP port
* easier access
* cleaner architecture

Users don't need to know internal app ports.

---

# INTERNAL KUBERNETES COMPONENTS WORKING

---

# kube-proxy

Handles:

* routing
* forwarding
* load balancing

Creates iptables/ipvs rules.

---

# CoreDNS

Handles:

```text id="tjlw41"
frontend-service
```

DNS resolution.

---

# Endpoints Object

Stores actual Pod IPs.

Example:

```text id="sjlw42"
frontend-service
  ↓
10.244.1.3:80
10.244.1.4:80
```

---

# CNI Plugin

Handles:

* Pod networking
* cross-node communication

Examples:

* Calico
* Flannel
* Cilium

---

# MOST IMPORTANT REAL PROJECT THINKING

Always think:

```text id="rjlw43"
Pods are temporary
Services are stable
```

---

# Why Service Important?

Pods may:

* die
* restart
* scale
* move nodes

Pod IP changes.

BUT:

```text id="qjlw44"
frontend-service
```

always remains same.

---

# REAL PRODUCTION FLOW

```text id="pjlw45"
Internet
   ↓
Ingress / LoadBalancer
   ↓
Frontend Service
   ↓
Frontend Pods
   ↓
Backend Service
   ↓
Backend Pods
```

---

# Final Most Important Understanding

```yaml
port: 80
```

= How clients access Service

---

```yaml
targetPort: 80
```

= Where Service forwards traffic inside Pods

---

```yaml
containerPort: 80
```

= Actual application port inside container

---

# Final Simple Mental Model

```text id="ojlw46"
LoadBalancer
     ↓
Service Port
     ↓
TargetPort
     ↓
ContainerPort
     ↓
Application
```
