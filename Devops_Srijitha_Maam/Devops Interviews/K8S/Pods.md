# 18. What is a Pod in Kubernetes?

## Simple Interview Answer

In Kubernetes, a **Pod** is the smallest deployable unit.

A pod is a wrapper around one or more containers.

Kubernetes does not directly run containers.
It runs containers inside pods.

---

# Why Pods are Needed?

Containers need:

* Networking
* Storage
* Communication
* Management

Pods provide these features.

You can think of a pod as:

> A small environment where containers run together.

---

# Pod Architecture

```text id="d5mjlwm"
Pod
 ├── Container 1
 ├── Container 2
 └── Shared Network & Storage
```

---

# Important Features of Pods

| Feature                  | Explanation                  |
| ------------------------ | ---------------------------- |
| Smallest Kubernetes Unit | Basic deployment object      |
| Contains Containers      | One or more containers       |
| Shared IP Address        | Containers share network     |
| Shared Storage           | Containers can share volumes |
| Temporary                | Pods can be recreated        |

---

# Single Container Pod

Most commonly:

* One pod contains one container.

Example:

```text id="jlwm4u"
Pod
 └── Nginx Container
```

---

# Multi-Container Pod

Sometimes a pod may contain multiple containers.

Example:

```text id="1jjlwm"
Pod
 ├── Application Container
 └── Logging Container
```

Both containers:

* Share same IP
* Share storage
* Communicate easily

---

# Why Pods are Temporary?

Pods are ephemeral.

If a pod crashes:

* Kubernetes recreates a new pod.

The new pod may get:

* New IP address
* New container instance

That’s why Kubernetes Services are used for stable communication.

---

# Pod Lifecycle

```text id="jlwm7r"
Create Pod
    ↓
Running
    ↓
Failed/Stopped
    ↓
Recreated by Kubernetes
```

---

# Sample Pod YAML File

## pod.yaml

```yaml id="jlwm92"
apiVersion: v1
kind: Pod

metadata:
  name: nginx-pod

spec:
  containers:
  - name: nginx-container
    image: nginx
    ports:
    - containerPort: 80
```

---

# Explanation of Pod YAML

---

# 1. apiVersion

```yaml id="jlwmr5"
apiVersion: v1
```

Defines Kubernetes API version.

---

# 2. kind

```yaml id="jlwm1h"
kind: Pod
```

Defines resource type.

Here:

* Pod resource

---

# 3. metadata

```yaml id="jlwm90"
metadata:
  name: nginx-pod
```

Defines pod name.

---

# 4. spec

Defines pod configuration.

---

# 5. containers

```yaml id="jlwm0f"
containers:
```

Defines containers inside pod.

---

# 6. image

```yaml id="jlwmv0"
image: nginx
```

Uses Nginx Docker image.

---

# How to Create a Pod

---

# Step 1: Apply YAML File

```bash id="jlwmfa"
kubectl apply -f pod.yaml
```

---

# Step 2: Check Pods

```bash id="jlwm0x"
kubectl get pods
```

---

# Step 3: Describe Pod

```bash id="jlwmpl"
kubectl describe pod nginx-pod
```

---

# Step 4: Delete Pod

```bash id="jlwmj4"
kubectl delete pod nginx-pod
```

---

# Pod Networking

Each pod gets:

* Unique IP address

Containers inside same pod:

* Communicate using localhost

---

# Pod Example in Real Life

Suppose an application has:

* Main application container
* Logging container

Both can run inside same pod because they work closely together.

---

# Pod vs Container

| Pod                             | Container                  |
| ------------------------------- | -------------------------- |
| Kubernetes object               | Runtime unit               |
| Can contain multiple containers | Single application process |
| Provides networking/storage     | Runs application           |

---

# Pod vs Deployment

| Pod                    | Deployment             |
| ---------------------- | ---------------------- |
| Single running unit    | Manages pods           |
| No auto-scaling        | Supports scaling       |
| Not self-healing alone | Self-healing supported |

In production:

* Deployments are preferred over standalone pods.

---

# Real-Time Example

Suppose a company runs:

* Nginx web application

Kubernetes creates:

* Multiple pods
* Each pod runs Nginx container

If one pod crashes:

* Kubernetes automatically creates another pod.

---

# Common Pod Commands

| Command                 | Purpose     |
| ----------------------- | ----------- |
| `kubectl get pods`      | List pods   |
| `kubectl describe pod`  | Pod details |
| `kubectl logs pod-name` | View logs   |
| `kubectl delete pod`    | Delete pod  |

---

# Important Interview Follow-Up Questions

---

## Can a Pod Have Multiple Containers?

Yes.

This is called:

* Multi-container pod

---

## Do Pods Have Fixed IPs?

No.

Pod IPs can change after restart.

---

## Why Pods are Used Instead of Containers Directly?

Pods provide:

* Networking
* Storage
* Lifecycle management

---

# Pod Architecture Diagram

```text id="jlwmcq"
Kubernetes Cluster
      ↓
Pod
      ↓
Container
      ↓
Application
```

---

# Short Interview Version (2-Minute Answer)

“A pod is the smallest deployable unit in Kubernetes. It is a wrapper around one or more containers. Kubernetes runs containers inside pods instead of directly running containers.

Pods provide shared networking and storage for containers. Usually one pod contains one container, but multiple containers can also run inside the same pod. Pods are temporary, and if a pod crashes, Kubernetes automatically recreates it.”
