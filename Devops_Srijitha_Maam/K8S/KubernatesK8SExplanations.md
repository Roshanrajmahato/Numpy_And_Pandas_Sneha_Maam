
# ☸️ Kubernetes Architecture — Complete Easy & Clean Understanding

---

# 🌍 What is Kubernetes?

Kubernetes is a platform that manages containers automatically.

Instead of manually:

* Starting containers
* Monitoring applications
* Restarting failed apps
* Scaling applications
* Managing networking
* Managing storage

Kubernetes handles everything automatically.

---

# 🧠 Core Idea of Kubernetes

Kubernetes mainly manages:

```text
Containers → Inside Pods → Running on Nodes
```

---

# 🏗️ Complete Kubernetes Architecture

```text
╔══════════════════════════════════════════════════════════════╗
║                    KUBERNETES CLUSTER                       ║
╚══════════════════════════════════════════════════════════════╝


                    ┌──────────────────────┐
                    │    CONTROL PLANE     │
                    │   (Brain of K8s)     │
                    ├──────────────────────┤
                    │ API Server           │
                    │ Scheduler            │
                    │ Controller Manager   │
                    │ etcd                 │
                    └──────────────────────┘
                               │
        ┌──────────────────────┴──────────────────────┐
        │                                             │


┌──────────────────────────────┐    ┌──────────────────────────────┐
│         WORKER NODE 1        │    │         WORKER NODE 2        │
│        (EC2 Instance)        │    │        (EC2 Instance)        │
├──────────────────────────────┤    ├──────────────────────────────┤
│ kubelet                      │    │ kubelet                      │
│ kube-proxy                   │    │ kube-proxy                   │
│ container runtime            │    │ container runtime            │
├──────────────────────────────┤    ├──────────────────────────────┤
│ Pod-A                        │    │ Pod-C                        │
│  └── Container               │    │  └── Container               │
│                              │    │                              │
│ Pod-B                        │    │ Pod-D                        │
│  └── Container               │    │  └── Container               │
└──────────────────────────────┘    └──────────────────────────────┘
```

---

# 🧠 Two Main Parts of Kubernetes

| Part             | Purpose          |
| ---------------- | ---------------- |
| 🎯 Control Plane | Makes decisions  |
| ⚙️ Worker Nodes  | Run applications |

---

# 🧠 Control Plane = Brain of Kubernetes

The Control Plane controls the entire cluster.

It decides:

✅ Where Pods should run
✅ When Pods restart
✅ How scaling happens
✅ Cluster health monitoring

---

# ⚙️ Worker Node = Machine Running Applications

A Worker Node is an actual machine.

Examples:

✅ AWS EC2 Instance
✅ Virtual Machine
✅ Physical Server

Worker Nodes run:

✅ Pods
✅ Containers
✅ Applications

---

# 🔥 MOST IMPORTANT UNDERSTANDING

Containers DO NOT run directly on Kubernetes nodes.

Correct architecture:

```text
EC2 Instance (Node)
    └── Pod
          └── Container
```

---

# 🧠 Real Kubernetes Flow

```text
Kubernetes Cluster
    └── Node (EC2 Instance)
            └── Pod
                    └── Container
```

---

# ❗ Very Important Correction

✅ Pod is NOT a container
✅ Pod is a wrapper for containers
✅ Containers run INSIDE Pods
✅ Pods run ON Nodes

---

# 📦 Pod Structure

A Pod can contain:

* One container
  OR
* Multiple containers

---

# 📦 Simple Pod Example

```text
Pod
├── nginx container
└── logging container
```

---

# 🌍 Real Example

Suppose:

```text
EC2 Worker Node
```

runs:

```text
Pod: nginx-pod
```

Inside that Pod:

```text
Container: nginx
```

So:

```text
Node
 └── Pod
      └── Container
```

---

# 🏢 Easy Real-World Analogy

| Kubernetes Component | Real World Analogy      |
| -------------------- | ----------------------- |
| EC2 Instance / Node  | Apartment Building      |
| Pod                  | Apartment               |
| Container            | Person inside apartment |

---

# 🧠 Analogy Understanding

```text
Building
   └── Apartments
          └── People
```

Similarly:

```text
Node
   └── Pods
          └── Containers
```

---

# 🔥 Why Kubernetes Uses Pods

Kubernetes uses Pods because Pods provide:

✅ Shared network
✅ Shared storage
✅ Lifecycle management
✅ Multi-container support

Kubernetes manages Pods, not individual containers directly.

---

# 🧠 Final Important Line

✅ Containers do NOT run directly on Nodes
✅ Containers run INSIDE Pods
✅ Pods run ON Nodes (EC2 instances)

---

# 🔄 Most Important Kubernetes Working Flow

```text
Developer Creates Deployment
              │
              ▼
API Server Receives Request
              │
              ▼
Configuration Stored in etcd
              │
              ▼
Scheduler Chooses Best Node
              │
              ▼
kubelet Receives Instruction
              │
              ▼
Container Runtime Pulls Image
              │
              ▼
Pod Starts on Node
              │
              ▼
Container Runs Inside Pod
              │
              ▼
Application Becomes Available
```

---

# 📦 Cluster

A Cluster is the complete Kubernetes environment.

```text
Cluster
├── Control Plane
└── Worker Nodes
```

Simple meaning:

> Everything together = Kubernetes Cluster

---

# 🖥️ Node

A Node is simply a machine.

Examples:

✅ AWS EC2 Instance
✅ VM
✅ Physical Server

Purpose:

✅ Provide CPU
✅ Provide RAM
✅ Run Pods

---

# 🚀 Pod (Most Important Concept)

A Pod is the smallest deployable unit in Kubernetes.

Pods contain containers.

---

# 📦 Pod Internal Structure

```text
Pod
├── Container-1
└── Container-2
```

---

# ⚡ Important Pod Properties

Containers inside same Pod:

✅ Share same IP
✅ Share same network namespace
✅ Share storage volumes

---

# ❗ Important Interview Point

Pods are temporary.

If Pod dies:

```text
Old Pod Deleted
        ↓
New Pod Created
        ↓
New IP Assigned
```

That is why Services are needed.

---

# ⚙️ Container Runtime

Container Runtime actually runs containers.

Without runtime:

```text
Containers Cannot Start
```

---

# 🔧 Common Container Runtimes

| Runtime    | Description          |
| ---------- | -------------------- |
| containerd | Most common          |
| CRI-O      | Kubernetes optimized |
| Docker     | Older setups         |

---

# 🔄 Runtime Flow

```text
kubelet
   │
   ▼
container runtime
   │
   ▼
Container starts
```

---

# 🤖 kubelet

kubelet runs on EVERY worker node.

Think of kubelet as:

> Node Manager

---

# ✅ kubelet Responsibilities

✅ Talks to Control Plane
✅ Receives Pod instructions
✅ Starts Pods
✅ Monitors containers
✅ Reports node health

---

# 🔄 kubelet Working Flow

```text
Control Plane
      │
      ▼
"Run Pod Here"
      │
      ▼
kubelet Receives Instruction
      │
      ▼
Container Runtime Starts Containers
```

---

# 🌐 kube-proxy

kube-proxy handles networking on nodes.

Responsibilities:

✅ Traffic forwarding
✅ Service networking
✅ Load balancing

---

# 🌍 Traffic Example

```text
Users
   │
   ▼
Service
   │
   ▼
┌───────┬───────┬───────┐
│ Pod-1 │ Pod-2 │ Pod-3 │
└───────┴───────┴───────┘
```

kube-proxy distributes traffic.

---

# 🎯 API Server

API Server is the ENTRY POINT of Kubernetes.

Everything talks to API Server.

---

# Example

```bash
kubectl apply -f app.yaml
```

Request goes to:

```text
API Server
```

---

# ✅ API Server Responsibilities

✅ Accept requests
✅ Validate requests
✅ Authenticate users
✅ Store data in etcd

---

# 🗄️ etcd

etcd is Kubernetes database.

Stores cluster state.

---

# 📚 etcd Stores

```text
Pods
Nodes
Secrets
Deployments
Services
Configs
```

---

# 🎯 Important Understanding

etcd stores:

> Desired State of Cluster

Example:

```text
Need 3 nginx Pods
```

Controllers ensure it becomes reality.

---

# 🧠 Scheduler

Scheduler decides:

> Which node should run the Pod?

---

# 📊 Scheduling Example

| Node   | Free RAM |
| ------ | -------- |
| Node-1 | 1GB      |
| Node-2 | 8GB      |

Pod requirement:

```text
4GB RAM
```

Scheduler selects:

```text
Node-2
```

---

# ✅ Scheduler Checks

✅ CPU
✅ RAM
✅ Node labels
✅ Affinity rules
✅ Taints & tolerations

---

# 🎛️ Controller Manager

Controllers continuously monitor the cluster.

Goal:

```text
Actual State = Desired State
```

---

# 📌 Example

Desired State:

```text
3 Pods Running
```

Actual State:

```text
2 Pods Running
```

Controller creates:

```text
1 New Pod
```

---

# 🌐 Service

Pods are temporary.

Services provide stable networking.

---

# ❌ Without Service

```text
Pod Restarts
      ↓
IP Changes
      ↓
Application Breaks
```

---

# ✅ With Service

Applications communicate using:

```text
Stable DNS Name
```

Example:

```text
frontend-service
```

---

# ✅ Service Provides

✅ Stable IP
✅ Stable DNS
✅ Load balancing

---

# 🔄 Service Traffic Flow

```text
User
  │
  ▼
Service
  │
  ▼
Available Pods
```

---

# 🚀 Deployment

Deployment manages Pods automatically.

---

# ✅ Deployment Features

✅ Scaling
✅ Rolling updates
✅ Self-healing
✅ Rollbacks

---

# Example

```yaml
replicas: 3
```

Meaning:

```text
Always Keep 3 Pods Running
```

---

# 📦 ReplicaSet

ReplicaSet maintains required Pod count.

If Pod dies:

```text
ReplicaSet Creates New Pod
```

Deployment internally uses ReplicaSet.

---

# 💾 Persistent Storage

Containers are temporary.

If container dies:

```text
Data May Be Lost
```

Persistent storage solves this.

---

# 💽 Persistent Volume (PV)

PV is actual storage.

Examples:

✅ AWS EBS
✅ NFS
✅ Ceph

---

# 📦 Persistent Volume Claim (PVC)

PVC requests storage.

Example:

```yaml
storage: 5Gi
```

---

# 🔄 Storage Flow

```text
Pod
 │
 ▼
PVC
 │
 ▼
PV
 │
 ▼
Actual Storage
```

---

# 🌍 Ingress

Ingress manages external HTTP/HTTPS traffic.

---

# ❌ Without Ingress

```text
One LoadBalancer Per App
```

Expensive.

---

# ✅ With Ingress

```text
Single Entry Point
```

Routes traffic:

```text
/app1 → Service-1
/app2 → Service-2
```

---

# 🌍 Real Production Flow

```text
Internet Users
        │
        ▼
Ingress
        │
        ▼
Service
        │
        ▼
Pods
        │
        ▼
Containers
```

Pods may run across multiple nodes.

Kubernetes automatically:

✅ Replaces failed Pods
✅ Balances traffic
✅ Scales applications
✅ Maintains desired state

---

# 📘 Best Short Definitions (Interview Revision)

| Component     | Easy Definition               |
| ------------- | ----------------------------- |
| Cluster       | Entire Kubernetes environment |
| Control Plane | Brain of Kubernetes           |
| Node          | Machine running Pods          |
| Pod           | Smallest deployable unit      |
| Container     | Actual application process    |
| kubelet       | Node agent                    |
| kube-proxy    | Networking manager            |
| Scheduler     | Chooses node for Pod          |
| etcd          | Kubernetes database           |
| Deployment    | Manages Pods                  |
| ReplicaSet    | Maintains Pod count           |
| Service       | Stable networking             |
| Ingress       | External HTTP router          |
| PV            | Persistent storage            |
| PVC           | Storage request               |
