# Kubernetes Service Files — Complete Detailed Explanation

In Kubernetes, a **Service YAML file** is used to define how applications (Pods) are exposed and communicated inside or outside the cluster.

A Service file contains:

* Service type
* Port configuration
* Pod selectors
* Networking rules
* Load balancing configuration

---

# Why We Write Service Files?

Pods are dynamic.

When Pods restart:

* IP changes
* Old connections break
* Communication fails

Service provides:

* Stable IP
* Stable DNS
* Automatic load balancing
* Reliable communication

---

# Real-Time Example

Suppose you have:

```text
Frontend Pods
Backend Pods
Database Pods
```

Without Service:

```text
Frontend → Pod IP directly
```

Problem:

If Backend Pod restarts:

```text
10.0.0.5 → 10.0.0.9
```

Frontend breaks.

---

# Solution Using Service

```text
Frontend
   ↓
backend-service
   ↓
Backend Pods
```

Frontend always talks to:

```text
backend-service
```

not Pod IPs.

---

# Basic Structure of Kubernetes Service File

```yaml
apiVersion: v1
kind: Service

metadata:
  name: my-service

spec:
  type: ClusterIP

  selector:
    app: myapp

  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

---

# Detailed Explanation of Every Field

---

# 1. apiVersion

```yaml
apiVersion: v1
```

Defines Kubernetes API version.

For Service:

```yaml
v1
```

is commonly used.

---

# 2. kind

```yaml
kind: Service
```

Tells Kubernetes:

```text
Create a Service object
```

Other kinds:

```yaml
Deployment
Pod
ConfigMap
Ingress
```

---

# 3. metadata

Stores Service information.

Example:

```yaml
metadata:
  name: backend-service
  namespace: production

  labels:
    app: backend
```

---

## metadata.name

```yaml
name: backend-service
```

Name of Service.

This becomes DNS name:

```text
backend-service.default.svc.cluster.local
```

---

## metadata.namespace

```yaml
namespace: production
```

Specifies namespace.

Without namespace:

```text
default namespace used
```

---

## metadata.labels

```yaml
labels:
  app: backend
```

Labels are identifiers.

Used for:

* organization
* filtering
* monitoring

---

# 4. spec Section

Most important part.

Defines:

* service type
* ports
* selectors
* networking behavior

---

# 5. type

Defines Service type.

Example:

```yaml
type: ClusterIP
```

Possible values:

| Type         | Purpose                |
| ------------ | ---------------------- |
| ClusterIP    | Internal communication |
| NodePort     | External access        |
| LoadBalancer | Cloud external access  |
| ExternalName | External DNS mapping   |

---

# 6. selector

Very important.

Example:

```yaml
selector:
  app: backend
```

Service finds Pods having:

```yaml
labels:
  app: backend
```

---

# How Selector Works

Pod:

```yaml
metadata:
  labels:
    app: backend
```

Service:

```yaml
selector:
  app: backend
```

Kubernetes automatically connects them.

---

# Internal Working

Service continuously watches Pods.

When new Pod comes:

```text
Automatically added to Service
```

When Pod dies:

```text
Automatically removed
```

This is called:

```text
Dynamic Endpoint Management
```

---

# 7. ports Section

Defines traffic rules.

Example:

```yaml
ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```

---

# Complete Port Flow

```text
User Request → Service Port → Target Port → Container
```

---

# port

```yaml
port: 80
```

Port exposed by Service.

Applications communicate with this port.

---

# targetPort

```yaml
targetPort: 8080
```

Actual container port.

Container application runs here.

---

# Example

Nginx container:

```yaml
containerPort: 8080
```

Service:

```yaml
port: 80
targetPort: 8080
```

Users access:

```text
Service:80
```

Traffic forwarded to:

```text
Container:8080
```

---

# protocol

```yaml
protocol: TCP
```

Possible values:

```text
TCP
UDP
SCTP
```

Default:

```text
TCP
```

---

# Full ClusterIP Service Example

```yaml
apiVersion: v1
kind: Service

metadata:
  name: backend-service

spec:
  type: ClusterIP

  selector:
    app: backend

  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

---

# How It Works Internally

```text
Frontend Pod
      ↓
backend-service:80
      ↓
Service forwards traffic
      ↓
Backend Pods:8080
```

---

# Kubernetes Automatically Creates

When Service is created:

Kubernetes creates:

* Virtual IP
* DNS entry
* Endpoint list
* iptables/ipvs rules

---

# kube-proxy Role

`kube-proxy` runs on every node.

It:

* watches Services
* watches Endpoints
* creates networking rules
* forwards traffic

---

# Endpoints

Endpoints = actual Pod IPs.

Example:

```text
10.244.0.5:8080
10.244.0.6:8080
10.244.0.7:8080
```

Command:

```bash
kubectl get endpoints
```

---

# Traffic Load Balancing

Suppose:

```text
3 backend pods
```

Traffic distribution:

```text
Request 1 → Pod1
Request 2 → Pod2
Request 3 → Pod3
```

Kubernetes does load balancing automatically.

---

# NodePort Service — Detailed

---

# YAML

```yaml
apiVersion: v1
kind: Service

metadata:
  name: nginx-service

spec:
  type: NodePort

  selector:
    app: nginx

  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007
```

---

# nodePort Field

```yaml
nodePort: 30007
```

Kubernetes opens this port on all nodes.

Accessible using:

```text
<NodeIP>:30007
```

---

# Internal Working

```text
Internet
   ↓
Node IP:30007
   ↓
kube-proxy
   ↓
Pods
```

---

# Important NodePort Range

Default range:

```text
30000–32767
```

---

# LoadBalancer Service — Detailed

---

# YAML

```yaml
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

# Internal Working

Cloud provider creates:

* External IP
* Load balancer
* Health checks

Flow:

```text
Internet
   ↓
Cloud Load Balancer
   ↓
Kubernetes Service
   ↓
Pods
```

---

# ExternalName Service — Detailed

---

# YAML

```yaml
apiVersion: v1
kind: Service

metadata:
  name: external-api

spec:
  type: ExternalName
  externalName: api.example.com
```

---

# How It Works

Kubernetes DNS returns:

```text
api.example.com
```

No proxying occurs.

---

# Headless Service

---

# YAML

```yaml
apiVersion: v1
kind: Service

metadata:
  name: mysql-headless

spec:
  clusterIP: None

  selector:
    app: mysql

  ports:
    - port: 3306
```

---

# Why Used?

Used for:

* StatefulSets
* Databases
* Direct Pod communication

---

# Difference Between Normal Service and Headless

| Feature           | Normal Service | Headless |
| ----------------- | -------------- | -------- |
| Cluster IP        | Yes            | No       |
| Load Balancing    | Yes            | No       |
| Direct Pod Access | No             | Yes      |

---

# Service Discovery

Kubernetes automatically creates DNS.

Format:

```text
<service-name>.<namespace>.svc.cluster.local
```

Example:

```text
backend.default.svc.cluster.local
```

Pods communicate using names instead of IPs.

---

# Multi-Port Service

Example:

```yaml
ports:
  - name: http
    port: 80
    targetPort: 8080

  - name: https
    port: 443
    targetPort: 8443
```

---

# Named Ports

Instead of numeric targetPort:

Pod:

```yaml
ports:
  - name: web
    containerPort: 8080
```

Service:

```yaml
targetPort: web
```

---

# Session Affinity

Keeps same user connected to same Pod.

```yaml
sessionAffinity: ClientIP
```

Useful for:

* login sessions
* shopping carts

---

# External Traffic Policy

```yaml
externalTrafficPolicy: Local
```

Options:

| Value   | Meaning            |
| ------- | ------------------ |
| Cluster | Default            |
| Local   | Preserve client IP |

---

# Service Without Selector

Possible to create Service without selectors.

Used for:

* external applications
* manual endpoint creation

Example:

```yaml
spec:
  ports:
    - port: 80
```

Then manually create endpoints.

---

# Service Lifecycle

---

# Step 1

Create Deployment:

```bash
kubectl apply -f deployment.yaml
```

---

# Step 2

Create Service:

```bash
kubectl apply -f service.yaml
```

---

# Step 3

Service finds Pods via selector.

---

# Step 4

Endpoints created automatically.

---

# Step 5

Traffic starts routing.

---

# Important Commands

---

# Create Service

```bash
kubectl apply -f service.yaml
```

---

# Get Services

```bash
kubectl get svc
```

---

# Describe Service

```bash
kubectl describe svc backend-service
```

---

# Get Endpoints

```bash
kubectl get endpoints
```

---

# Delete Service

```bash
kubectl delete svc backend-service
```

---

# Expose Deployment

```bash
kubectl expose deployment nginx \
--type=NodePort \
--port=80
```

---

# Real Production Architecture

```text
Internet
   ↓
Ingress
   ↓
LoadBalancer Service
   ↓
Frontend Pods
   ↓
ClusterIP Service
   ↓
Backend Pods
   ↓
Database
```

---

# How Ingress and Service Work Together

Ingress handles:

* HTTP routing
* domain names
* SSL termination

Service handles:

* Pod networking
* load balancing

---

# Best Practices

| Best Practice                | Reason          |
| ---------------------------- | --------------- |
| Use ClusterIP internally     | Security        |
| Use Ingress + LoadBalancer   | Production      |
| Use labels properly          | Easy management |
| Avoid NodePort in production | Security issues |
| Use namespaces               | Isolation       |

---

# Common Problems

---

# 1. Service Not Finding Pods

Cause:

Selector mismatch.

Check:

```bash
kubectl get pods --show-labels
```

---

# 2. Port Not Working

Cause:

Wrong targetPort.

---

# 3. No External Access

Cause:

Firewall/security group issue.

---

# 4. Endpoint Empty

Cause:

No matching Pods.

---

# Full Production Example

---

# Backend Deployment

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: backend

spec:
  replicas: 3

  selector:
    matchLabels:
      app: backend

  template:
    metadata:
      labels:
        app: backend

    spec:
      containers:
        - name: backend
          image: myapp:v1

          ports:
            - containerPort: 8080
```

---

# Backend Service

```yaml
apiVersion: v1
kind: Service

metadata:
  name: backend-service

spec:
  type: ClusterIP

  selector:
    app: backend

  ports:
    - port: 80
      targetPort: 8080
```

---

# End-to-End Traffic Flow

```text
User
 ↓
Ingress
 ↓
Service
 ↓
kube-proxy
 ↓
Endpoints
 ↓
Pods
 ↓
Container Application
```

---

# Interview-Level Summary

“Kubernetes Service is an abstraction layer that provides stable networking and load balancing for Pods. Since Pod IPs are dynamic, Services provide fixed IPs and DNS names for communication.

Services work using labels and selectors. kube-proxy maintains networking rules and forwards traffic to pod endpoints.

The main Service types are ClusterIP, NodePort, LoadBalancer, and ExternalName.”
