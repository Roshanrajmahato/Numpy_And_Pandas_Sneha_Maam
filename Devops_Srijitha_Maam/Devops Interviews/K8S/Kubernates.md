# 13. What is Kubernetes and Why is it Used? Write a Sample Deployment File.

## Simple Interview Answer

Kubernetes, also called **K8s**, is an open-source container orchestration platform used to:

* Deploy containers
* Manage containers
* Scale applications
* Monitor containerized applications automatically

It was originally developed by:

* Google

### Official Website

[Kubernetes](https://kubernetes.io?utm_source=chatgpt.com)

Kubernetes is mainly used to manage Docker containers in production environments.

---

# Why Kubernetes is Needed?

Suppose an application has:

* 100 containers
* Multiple servers
* High traffic

Managing containers manually becomes difficult.

Problems:

* Container crashes
* Scaling issues
* Load balancing complexity
* Deployment management

Kubernetes solves these problems using automation.

---

# What Kubernetes Does

Kubernetes automates:

* Container deployment
* Scaling
* Load balancing
* Self-healing
* Rolling updates

---

# Why Kubernetes is Used?

| Purpose                 | Explanation                      |
| ----------------------- | -------------------------------- |
| Container Orchestration | Manages containers automatically |
| Auto Scaling            | Increase/decrease containers     |
| High Availability       | Applications remain available    |
| Self-Healing            | Restarts failed containers       |
| Load Balancing          | Distributes traffic              |
| Rolling Updates         | Update app without downtime      |

---

# Kubernetes Architecture

Kubernetes has:

1. Master Node (Control Plane)
2. Worker Nodes

---

# 1. Master Node

Controls the cluster.

### Components

| Component          | Purpose                 |
| ------------------ | ----------------------- |
| API Server         | Entry point             |
| Scheduler          | Assigns pods            |
| Controller Manager | Maintains desired state |
| ETCD               | Stores cluster data     |

---

# 2. Worker Node

Runs application containers.

### Components

| Component         | Purpose                  |
| ----------------- | ------------------------ |
| Kubelet           | Communicates with master |
| Kube Proxy        | Networking               |
| Container Runtime | Runs containers          |

---

# Important Kubernetes Concepts

---

# 1. Pod

Smallest deployable unit in Kubernetes.

A pod contains:

* One or more containers

Example:

```text id="d4x4o4"
Pod
 └── Nginx Container
```

---

# 2. Deployment

Deployment manages pods.

Features:

* Scaling
* Updates
* Self-healing

---

# 3. Service

Service exposes application to users or other applications.

---

# 4. Namespace

Used to logically separate resources.

---

# Kubernetes Workflow

```text id="pk4j6r"
Developer Creates Docker Image
            ↓
Push Image to Docker Registry
            ↓
Kubernetes Deployment File
            ↓
Pods Created
            ↓
Application Runs
```

---

# Sample Kubernetes Deployment File

## deployment.yaml

```yaml id="i0rzm2"
apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx-deployment

spec:
  replicas: 3

  selector:
    matchLabels:
      app: nginx

  template:
    metadata:
      labels:
        app: nginx

    spec:
      containers:
      - name: nginx-container
        image: nginx:latest

        ports:
        - containerPort: 80
```

---

# Explanation of Deployment File

---

# 1. apiVersion

```yaml id="f0yoj7"
apiVersion: apps/v1
```

### Purpose

Defines Kubernetes API version.

---

# 2. kind

```yaml id="3m4c20"
kind: Deployment
```

### Purpose

Specifies resource type.

Here:

* Deployment resource

---

# 3. metadata

```yaml id="kh6w7m"
metadata:
  name: nginx-deployment
```

### Purpose

Defines deployment name.

---

# 4. replicas

```yaml id="ivp39c"
replicas: 3
```

### Purpose

Creates 3 pod replicas.

Benefits:

* High availability
* Load balancing

---

# 5. selector

```yaml id="w6jvri"
selector:
  matchLabels:
```

### Purpose

Connects deployment to matching pods.

---

# 6. template

Defines pod configuration.

---

# 7. containers

```yaml id="l1rx6g"
containers:
```

### Purpose

Defines containers inside pod.

---

# 8. image

```yaml id="g3i4ax"
image: nginx:latest
```

### Purpose

Uses Nginx Docker image.

---

# 9. containerPort

```yaml id="8s8vth"
containerPort: 80
```

### Purpose

Exposes container port.

---

# How to Deploy in Kubernetes

---

# Step 1: Apply Deployment File

```bash id="b4i1r4"
kubectl apply -f deployment.yaml
```

---

# Step 2: Check Pods

```bash id="yxz5sm"
kubectl get pods
```

---

# Step 3: Check Deployments

```bash id="j2z1q3"
kubectl get deployments
```

---

# Step 4: Expose Deployment

```bash id="y0v1yu"
kubectl expose deployment nginx-deployment --type=NodePort --port=80
```

---

# Important Kubernetes Features

| Feature           | Explanation                |
| ----------------- | -------------------------- |
| Auto Healing      | Restarts failed pods       |
| Auto Scaling      | Increase/decrease replicas |
| Rolling Updates   | Zero downtime updates      |
| Service Discovery | Easy communication         |
| Load Balancing    | Traffic distribution       |

---

# Real-Time Example

Suppose an e-commerce website receives huge traffic during a sale.

Kubernetes automatically:

* Creates more pods
* Balances traffic
* Restarts failed containers

This keeps the application stable.

---

# Kubernetes vs Docker

| Docker                    | Kubernetes             |
| ------------------------- | ---------------------- |
| Runs containers           | Manages containers     |
| Single container platform | Orchestration platform |
| Container creation        | Container management   |

---

# Common Kubernetes Commands

| Command                   | Purpose          |
| ------------------------- | ---------------- |
| `kubectl get pods`        | List pods        |
| `kubectl get deployments` | List deployments |
| `kubectl apply -f`        | Apply YAML file  |
| `kubectl delete -f`       | Delete resources |
| `kubectl describe pod`    | Pod details      |

---

# Kubernetes Service Types

| Service      | Purpose                  |
| ------------ | ------------------------ |
| ClusterIP    | Internal communication   |
| NodePort     | External access          |
| LoadBalancer | Cloud load balancer      |
| ExternalName | External service mapping |

---

# Important Interview Follow-Up Questions

---

## What Happens if Pod Crashes?

Kubernetes automatically recreates it.

---

## Why Replicas are Used?

For:

* High availability
* Load balancing
* Fault tolerance

---

## What is Rolling Update?

Updates application gradually without downtime.

---

# Kubernetes Architecture Diagram

```text id="8ltjq0"
Master Node
    ↓
Worker Nodes
    ↓
Pods
    ↓
Containers
```

---

# Short Interview Version (2-Minute Answer)

“Kubernetes is an open-source container orchestration platform used to deploy, manage, scale, and monitor containerized applications. It automates container management tasks like scaling, self-healing, load balancing, and rolling updates.

A Kubernetes deployment file defines how containers should run, including replicas, container images, and ports. Kubernetes is widely used in production environments to manage Docker containers efficiently.”
