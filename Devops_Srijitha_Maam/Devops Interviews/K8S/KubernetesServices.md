# 16. Types of Kubernetes Services

## Simple Interview Answer

In Kubernetes, a Service is used to expose applications running inside pods.

Pods are temporary and their IP addresses can change, so Kubernetes Services provide:

* Stable networking
* Load balancing
* Service discovery

The main types of Kubernetes Services are:

1. ClusterIP
2. NodePort
3. LoadBalancer
4. ExternalName

---

# Why Kubernetes Services are Needed?

Pods in Kubernetes are dynamic.

Problems without Services:

* Pod IP changes after restart
* Difficult communication between applications
* No stable access point

Services solve these issues by providing a permanent endpoint.

---

# Kubernetes Service Workflow

```text id="mw5t9m"
User Request
     ↓
Kubernetes Service
     ↓
Pod 1
Pod 2
Pod 3
```

Service automatically distributes traffic among pods.

---

# 1. ClusterIP Service

## What is ClusterIP?

ClusterIP is the default Kubernetes Service type.

It exposes the application internally within the Kubernetes cluster.

---

## Characteristics

| Feature         | Description |
| --------------- | ----------- |
| Internal Access | Yes         |
| External Access | No          |
| Default Type    | Yes         |
| Load Balancing  | Yes         |

---

## Use Case

Used for:

* Backend services
* Database communication
* Internal microservices

---

## Example YAML

```yaml id="t4nq2s"
apiVersion: v1
kind: Service

metadata:
  name: my-service

spec:
  type: ClusterIP

  selector:
    app: nginx

  ports:
    - port: 80
      targetPort: 80
```

---

# ClusterIP Architecture

```text id="36mjlwm"
Frontend Pod
      ↓
ClusterIP Service
      ↓
Backend Pods
```

---

# 2. NodePort Service

## What is NodePort?

NodePort exposes the application externally using a port on each Kubernetes node.

Kubernetes opens a port range:

```text id="0qjlwm"
30000–32767
```

---

## Characteristics

| Feature         | Description |
| --------------- | ----------- |
| Internal Access | Yes         |
| External Access | Yes         |
| Port Range      | 30000–32767 |

---

## Example YAML

```yaml id="nhr2y8"
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

## Access Example

```text id="jlwm8d"
http://NodeIP:30007
```

---

## Use Case

Used for:

* Testing
* Development environments

---

# 3. LoadBalancer Service

## What is LoadBalancer?

LoadBalancer exposes applications externally using a cloud provider’s load balancer.

Commonly used in:

* AWS
* Azure
* GCP

---

## Characteristics

| Feature                 | Description |
| ----------------------- | ----------- |
| External Access         | Yes         |
| Cloud Integration       | Yes         |
| Automatic Load Balancer | Yes         |

---

## Example YAML

```yaml id="o0quq0"
apiVersion: v1
kind: Service

metadata:
  name: nginx-loadbalancer

spec:
  type: LoadBalancer

  selector:
    app: nginx

  ports:
    - port: 80
      targetPort: 80
```

---

## Use Case

Used in production environments for:

* Web applications
* Public APIs

---

# LoadBalancer Workflow

```text id="2osg9q"
Internet
    ↓
Cloud Load Balancer
    ↓
Kubernetes Service
    ↓
Pods
```

---

# 4. ExternalName Service

## What is ExternalName?

ExternalName maps a Kubernetes Service to an external DNS name.

No proxying happens.

---

## Example YAML

```yaml id="1ph48j"
apiVersion: v1
kind: Service

metadata:
  name: external-service

spec:
  type: ExternalName
  externalName: example.com
```

---

## Use Case

Used to connect Kubernetes applications to:

* External databases
* External APIs
* Third-party services

---

# Comparison of Kubernetes Service Types

| Service Type | Internal Access | External Access | Use Case               |
| ------------ | --------------- | --------------- | ---------------------- |
| ClusterIP    | Yes             | No              | Internal communication |
| NodePort     | Yes             | Yes             | Testing                |
| LoadBalancer | Yes             | Yes             | Production             |
| ExternalName | External DNS    | External DNS    | External services      |

---

# Which is Default Kubernetes Service?

# ClusterIP

If no type is specified, Kubernetes automatically creates a ClusterIP service.

---

# Real-Time Example

Suppose an e-commerce application has:

* Frontend pods
* Backend pods
* Database pods

### Usage

| Component | Service Type |
| --------- | ------------ |
| Frontend  | LoadBalancer |
| Backend   | ClusterIP    |
| Database  | ClusterIP    |

This keeps backend and database secure inside cluster.

---

# Kubernetes Service Commands

| Command                     | Purpose         |
| --------------------------- | --------------- |
| `kubectl get services`      | List services   |
| `kubectl describe service`  | Service details |
| `kubectl expose deployment` | Create service  |

---

# Important Interview Follow-Up Questions

---

## Difference Between NodePort and LoadBalancer

| NodePort              | LoadBalancer              |
| --------------------- | ------------------------- |
| Uses node IP and port | Uses cloud load balancer  |
| Manual access         | Automatic external access |
| Good for testing      | Good for production       |

---

## Why ClusterIP is Default?

Because most applications require internal communication between services.

---

## What is Service Discovery?

Kubernetes automatically allows services to communicate using service names.

Example:

```text id="qfc6gf"
backend-service.default.svc.cluster.local
```

---

# Kubernetes Networking Example

```text id="58wvkh"
User
 ↓
LoadBalancer
 ↓
Frontend Pods
 ↓
ClusterIP Service
 ↓
Backend Pods
```

---

# Short Interview Version (2-Minute Answer)

“Kubernetes Services are used to expose applications running inside pods and provide stable networking and load balancing.

The main service types are ClusterIP, NodePort, LoadBalancer, and ExternalName. ClusterIP is the default service type and is used for internal communication. NodePort exposes applications using node ports, LoadBalancer provides external access through cloud load balancers, and ExternalName connects services to external DNS names.”
