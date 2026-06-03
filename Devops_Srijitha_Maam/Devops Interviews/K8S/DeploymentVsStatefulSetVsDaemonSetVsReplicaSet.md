# 17. Difference Between Deployment, StatefulSet, DaemonSet, and ReplicaSet

## Simple Interview Answer

In Kubernetes, Deployment, StatefulSet, DaemonSet, and ReplicaSet are Kubernetes workload controllers used to manage pods.

Each controller has a different purpose:

* **Deployment** → Manages stateless applications
* **StatefulSet** → Manages stateful applications
* **DaemonSet** → Runs one pod on every node
* **ReplicaSet** → Maintains a fixed number of pod replicas

---

# Why Kubernetes Controllers are Needed?

Pods are temporary.

If a pod crashes:

* Kubernetes should recreate it automatically.

Controllers help:

* Maintain desired state
* Scale applications
* Manage updates
* Ensure availability

---

# 1. Deployment

## What is Deployment?

Deployment is the most commonly used Kubernetes controller.

It manages:

* Stateless applications
* Scaling
* Rolling updates
* Self-healing

---

## Features of Deployment

| Feature         | Description |
| --------------- | ----------- |
| Stateless Apps  | Yes         |
| Auto Scaling    | Yes         |
| Rolling Updates | Yes         |
| Self-Healing    | Yes         |

---

## Use Cases

Used for:

* Web applications
* APIs
* Frontend services

Examples:

* Nginx
* Node.js apps
* React apps

---

## Example Deployment YAML

```yaml id="sl2h70"
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
      - name: nginx
        image: nginx
```

---

## Deployment Workflow

```text id="kw6o9n"
Deployment
     ↓
ReplicaSet
     ↓
Pods
```

Deployment internally creates ReplicaSets.

---

# 2. StatefulSet

## What is StatefulSet?

StatefulSet manages stateful applications where each pod requires:

* Stable identity
* Persistent storage
* Ordered deployment

---

## Features of StatefulSet

| Feature            | Description |
| ------------------ | ----------- |
| Stateful Apps      | Yes         |
| Stable Pod Names   | Yes         |
| Persistent Storage | Yes         |
| Ordered Deployment | Yes         |

---

## Use Cases

Used for:

* Databases
* Kafka
* Elasticsearch
* MongoDB

---

## Example

Pods created like:

```text id="jlwm0m"
mysql-0
mysql-1
mysql-2
```

Each pod keeps:

* Same name
* Same storage

even after restart.

---

## Example StatefulSet YAML

```yaml id="q1h0vu"
apiVersion: apps/v1
kind: StatefulSet

metadata:
  name: mysql

spec:
  serviceName: mysql
  replicas: 3

  selector:
    matchLabels:
      app: mysql

  template:
    metadata:
      labels:
        app: mysql

    spec:
      containers:
      - name: mysql
        image: mysql:5.7
```

---

# Why StatefulSet is Important?

Databases require:

* Persistent data
* Unique identities

Deployment cannot guarantee this.

---

# 3. DaemonSet

## What is DaemonSet?

DaemonSet ensures that one pod runs on every node in the cluster.

If a new node is added:

* Kubernetes automatically creates the pod there.

---

## Features of DaemonSet

| Feature                 | Description |
| ----------------------- | ----------- |
| One Pod Per Node        | Yes         |
| Automatic Node Coverage | Yes         |
| Background Services     | Yes         |

---

## Use Cases

Used for:

* Monitoring agents
* Log collectors
* Security agents

Examples:

* Fluentd
* Prometheus Node Exporter

---

## Example DaemonSet Workflow

```text id="jlwmg4"
Node 1 → Monitoring Pod
Node 2 → Monitoring Pod
Node 3 → Monitoring Pod
```

---

## Example DaemonSet YAML

```yaml id="zbqixf"
apiVersion: apps/v1
kind: DaemonSet

metadata:
  name: monitoring-agent

spec:
  selector:
    matchLabels:
      app: monitor

  template:
    metadata:
      labels:
        app: monitor

    spec:
      containers:
      - name: monitor
        image: fluentd
```

---

# 4. ReplicaSet

## What is ReplicaSet?

ReplicaSet ensures a fixed number of pod replicas are always running.

If a pod crashes:

* ReplicaSet recreates it automatically.

---

## Features of ReplicaSet

| Feature             | Description |
| ------------------- | ----------- |
| Maintains Pod Count | Yes         |
| Self-Healing        | Yes         |
| Scaling             | Basic       |

---

## Example

Suppose:

```yaml id="jlwm30"
replicas: 3
```

If one pod fails:

* ReplicaSet automatically creates another pod.

---

## Important Point

In real-world production:

* Deployments are mostly used instead of ReplicaSets directly.

Because Deployment provides:

* Rolling updates
* Easier management

---

## Example ReplicaSet YAML

```yaml id="3fe4s1"
apiVersion: apps/v1
kind: ReplicaSet

metadata:
  name: myapp-replicaset

spec:
  replicas: 3

  selector:
    matchLabels:
      app: myapp

  template:
    metadata:
      labels:
        app: myapp

    spec:
      containers:
      - name: myapp
        image: nginx
```

---

# Main Difference Table

| Feature            | Deployment     | StatefulSet   | DaemonSet        | ReplicaSet         |
| ------------------ | -------------- | ------------- | ---------------- | ------------------ |
| Purpose            | Stateless apps | Stateful apps | One pod per node | Maintain replicas  |
| Stable Identity    | No             | Yes           | No               | No                 |
| Persistent Storage | Optional       | Important     | Optional         | Optional           |
| Rolling Updates    | Yes            | Yes           | Yes              | Limited            |
| Auto Scaling       | Yes            | Yes           | Node-based       | Basic              |
| Common Use         | Web apps       | Databases     | Monitoring       | Replica management |

---

# Real-Time Example

Suppose a company runs:

* Frontend app
* MySQL database
* Monitoring system

### Kubernetes Controllers Used

| Application        | Controller  |
| ------------------ | ----------- |
| Frontend App       | Deployment  |
| MySQL Database     | StatefulSet |
| Monitoring Agent   | DaemonSet   |
| Replica Management | ReplicaSet  |

---

# Important Interview Follow-Up Questions

---

## Why Deployment Uses ReplicaSet?

Deployment internally manages ReplicaSets for:

* Scaling
* Updates
* Rollbacks

---

## Why Databases Use StatefulSet?

Because databases require:

* Persistent storage
* Stable network identity

---

## Why DaemonSet is Used for Monitoring?

Monitoring agents must run on every node.

---

# Controller Architecture

```text id="jlwm3q"
Deployment
    ↓
ReplicaSet
    ↓
Pods
```

---

# Production Example

Monitoring stack:

* Prometheus
* Grafana

Often uses:

* DaemonSets for node monitoring

Databases:

* MongoDB
* MySQL

Often use:

* StatefulSets

---

# Short Interview Version (2-Minute Answer)

“Deployment, StatefulSet, DaemonSet, and ReplicaSet are Kubernetes controllers used to manage pods.

Deployment is used for stateless applications and supports scaling and rolling updates. StatefulSet is used for stateful applications like databases where stable identity and persistent storage are required. DaemonSet ensures one pod runs on every node and is commonly used for monitoring agents. ReplicaSet maintains a fixed number of pod replicas and provides self-healing functionality.”
