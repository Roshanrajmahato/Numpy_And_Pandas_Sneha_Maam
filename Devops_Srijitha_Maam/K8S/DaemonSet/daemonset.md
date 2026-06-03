[ DAEMONSET OBJECT IN K8S CHATGPT LINK](https://chatgpt.com/c/697d8c8f-4854-8322-9195-839f8cd35a32)

# Prometheus 

Prometheus – Step by Step

Create files
node-exporter-daemonset.yaml
prometheus-config.yaml
prometheus-deployment.yaml
prometheus-service.yaml

1. Create Namespace
>runcmd
       > ` kubectl create namespace monitoring `

2. Apply All YAMLs
```bash

kubectl apply -f node-exporter-daemonset.yaml
kubectl apply -f prometheus-config.yaml
kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-service.yaml

```

3. Verify Check DaemonSet
>runcmd
       > `  kubectl get daemonset -n monitoring  `

4. Check Pods  
>runcmd 
       > `   kubectl get pods -n monitoring -o wide   `
You will see 
node-exporter pod on each node
one prometheus pod aslo

5. Check Service :- 1 prometheus pod you will find
>runcmd 
       > ` kubectl get svc -n monitoring `


# Grafana

Grafana Step by Step :-

Create files
grafana-datasource.yaml
grafana-deployment.yaml
grafana-service.yaml


1.  Apply YAMLs

```bash

kubectl apply -f grafana-datasource.yaml
kubectl apply -f grafana-deployment.yaml
kubectl apply -f grafana-service.yaml

```

2. Verify pods
>runcmd
       > ` kubectl get pods -n monitoring `
       > ` kubectl get pods -n monitoring -o wide   `

You should see :-
prometheus pod 
node-exporter pods 
grafana pod  running their

3. Check Services  for Port Mapping
>runcmd
       >  ` kubectl get svc -n monitoring `

You will see 
grafana  NodePort  30300

4. Login to Grafana

Open in browser:-
http://<any-node-ip>:30300
http://65.2.137.107:30300


Then Login The Graphana by these credencial
user: admin
pass: admin

It will ask to change password → set anything.


5. For Checking The Pods and PV and PVC

```bash

kubectl get pods -o wide
kubectl get pv
kubectl get pvc
kubectl describe pvc ebs-pvc


```

6. For Checking  pods and svc in the  Namespace(monitoring)

```bash

kubectl get pods -n monitoring -o wide
kubectl get svc -n monitoring

```

kubectl get pods 
kubectl get pv
kubectl get pvc
kubectl get pods -n monitoring 
kubectl get svc -n monitoring



Nice question Roshan 👍 — this is a **real production-level use case**, and it will help you in interviews + your DevOps projects.

I will explain in this flow:

1. ✅ Complete YAML files
2. Step-by-step deployment
3. How monitoring actually works
4. How Prometheus collects metrics
5. Verification commands
6. Architecture explanation

---

# 🔴 1. What We Are Going to Do

We will deploy:

* ✅ Node Exporter → using **DaemonSet** (runs on every node)
* ✅ Prometheus Server → using **Deployment + Service**
* ✅ Prometheus will scrape metrics from Node Exporter

👉 Goal: Monitor CPU, RAM, Disk, Network of every node.

---

# 🔴 2. Complete YAML Files

## (A) Node Exporter – DaemonSet

📁 file: `node-exporter-daemonset.yaml`

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: monitoring
  labels:
    app: node-exporter
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      hostNetwork: true
      containers:
      - name: node-exporter
        image: prom/node-exporter:latest
        ports:
        - containerPort: 9100
          name: metrics
```

### Line by Line Explanation

* `kind: DaemonSet`

  * Ensures 1 pod on every node

* `namespace: monitoring`

  * We separate monitoring components from app

* `hostNetwork: true`

  * Node exporter reads node metrics directly
  * Needs host network access

* `image: prom/node-exporter`

  * Official exporter image

* `containerPort: 9100`

  * Metrics are exposed on this port

---

## (B) Prometheus ConfigMap

📁 `prometheus-config.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: monitoring
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s

    scrape_configs:
      - job_name: 'node-exporter'
        static_configs:
          - targets: ['node-exporter:9100']
```

### Explanation

* `scrape_interval: 15s`

  * Prometheus will collect metrics every 15 sec

* `job_name`

  * Logical name in Prometheus

* `targets`

  * From where to collect metrics

---

## (C) Prometheus Deployment

📁 `prometheus-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      containers:
      - name: prometheus
        image: prom/prometheus:latest
        args:
          - "--config.file=/etc/prometheus/prometheus.yml"
        ports:
        - containerPort: 9090
        volumeMounts:
        - name: config
          mountPath: /etc/prometheus
      volumes:
      - name: config
        configMap:
          name: prometheus-config
```

---

## (D) Prometheus Service

📁 `prometheus-service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: prometheus
  namespace: monitoring
spec:
  type: NodePort
  selector:
    app: prometheus
  ports:
  - port: 9090
    targetPort: 9090
    nodePort: 30090
```

👉 Access Prometheus at:

```
http://<NodeIP>:30090
```

---

# 🔴 3. How to Perform – Step by Step

## Step 1 – Create Namespace

```bash
kubectl create namespace monitoring
```

---

## Step 2 – Apply All YAMLs

```bash
kubectl apply -f node-exporter-daemonset.yaml
kubectl apply -f prometheus-config.yaml
kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-service.yaml
```

---

## Step 3 – Verify

### Check DaemonSet

```bash
kubectl get daemonset -n monitoring
```

Output:

```
node-exporter  3/3
```

👉 3 nodes = 3 pods automatically

---

### Check Pods

```bash
kubectl get pods -n monitoring -o wide
```

You will see:

* node-exporter pod on each node
* 1 prometheus pod

---

### Check Service

```bash
kubectl get svc -n monitoring
```

---

# 🔴 4. How Monitoring Actually Works (Concept)

## Architecture

```
[Node 1] ----> node-exporter:9100 ----\
[Node 2] ----> node-exporter:9100 ----- > Prometheus Server
[Node 3] ----> node-exporter:9100 ----/
```

### Flow

1. Node Exporter

   * Reads:

     * CPU usage
     * Memory
     * Disk
     * Network
   * Exposes as HTTP metrics

2. Prometheus

   * Calls:

     ```
     http://node-ip:9100/metrics
     ```
   * Stores data as time-series

---

# 🔴 5. Test Manually

## Open metrics of any node

```bash
curl http://<node-ip>:9100/metrics
```

You will see:

```
node_cpu_seconds_total
node_memory_MemAvailable
node_disk_io_time_seconds
```

---

## In Prometheus UI

Open:

```
http://<NodeIP>:30090
```

### Try Queries

👉 CPU usage

```
rate(node_cpu_seconds_total[1m])
```

👉 Memory

```
node_memory_MemAvailable_bytes
```

👉 Disk

```
node_disk_read_bytes_total
```

---

# 🔴 6. Interview Level Explanation

### Q: Why DaemonSet for Node Exporter?

👉 Because:

* Need 1 exporter per node
* New node → auto monitoring
* Node delete → auto cleanup

---

### Q: Difference

| Deployment        | DaemonSet       |
| ----------------- | --------------- |
| Manual replicas   | Auto per node   |
| Not node specific | Node specific   |
| App workloads     | Infra workloads |

---

# 🔴 7. Real Production Add-ons

Next we can add:

* Grafana dashboard
* AlertManager
* ServiceMonitor (Prometheus Operator)
* Helm based install

---

## 🚀 Next Step Roshan

Tell me:

👉 Are you using:

* Minikube?
* kubeadm cluster?
* cloud (EKS/AKS/GKE)?

I will tune YAML according to your environment and also help you add:

* Grafana dashboards
* CPU alert
* Memory alert
* WhatsApp/Email alerts


Great Roshan 👍 — since you are on **kubeadm cluster (bare metal / VM based)**, I will give you:

✅ Grafana YAML tuned for kubeadm
✅ It will connect with your existing Prometheus
✅ NodePort based access (best for kubeadm)
✅ Proper data source auto configuration

I’ll provide:

1. Grafana Deployment YAML
2. Grafana Service YAML
3. Auto Prometheus DataSource Config
4. Step-by-step commands
5. How to import dashboards

---

# 🔴 1. Grafana ConfigMap (Auto Add Prometheus)

📁 `grafana-datasource.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-datasource
  namespace: monitoring
  labels:
    grafana_datasource: "1"
data:
  prometheus.yaml: |
    apiVersion: 1
    datasources:
    - name: Prometheus
      type: prometheus
      access: proxy
      url: http://prometheus:9090
      isDefault: true
```

### Why This?

👉 When Grafana starts:

* It will automatically add
* Prometheus as datasource
* No manual UI configuration needed

---

# 🔴 2. Grafana Deployment

📁 `grafana-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      labels:
        app: grafana
    spec:
      containers:
      - name: grafana
        image: grafana/grafana:latest
        ports:
        - containerPort: 3000

        volumeMounts:
        - name: datasource
          mountPath: /etc/grafana/provisioning/datasources

      volumes:
      - name: datasource
        configMap:
          name: grafana-datasource
```

---

# 🔴 3. Grafana Service (NodePort – kubeadm friendly)

📁 `grafana-service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: grafana
  namespace: monitoring
spec:
  type: NodePort
  selector:
    app: grafana
  ports:
  - port: 3000
    targetPort: 3000
    nodePort: 30300
```

👉 Access URL:

```
http://<ANY_NODE_IP>:30300
```

---

# 🔴 4. Apply Step by Step

## Step 1 – Apply YAMLs

```bash
kubectl apply -f grafana-datasource.yaml
kubectl apply -f grafana-deployment.yaml
kubectl apply -f grafana-service.yaml
```

---

## Step 2 – Verify

```bash
kubectl get pods -n monitoring
```

You should see:

* prometheus pod
* node-exporter pods
* grafana pod ✅

---

```bash
kubectl get svc -n monitoring
```

You will see:

```
grafana  NodePort  30300
```

---

# 🔴 5. Login to Grafana

Open in browser:

```
http://<kubeadm-node-ip>:30300
```

### Default Login

* user: admin
* pass: admin

It will ask to change password → set anything.

---

# 🔴 6. Import Node Exporter Dashboard

### Best Dashboard ID

👉 1860 – Node Exporter Full

## Steps in UI

1. Open Grafana
2. Click ➜ Dashboards
3. Import
4. Enter ID:

```
1860
```

5. Select datasource → Prometheus
6. BOOM 💥

You get:

* CPU usage
* Memory
* Disk IO
* Network
* Per node stats

---

# 🔴 7. Complete Architecture Now

```
[Each Node]
   |
   |-- Node Exporter (DaemonSet) :9100
           |
           v
      Prometheus :9090
           |
           v
      Grafana :3000
```

---

# 🔴 8. Real Monitoring Queries Used by Dashboard

### CPU

```
rate(node_cpu_seconds_total[1m])
```

### Memory

```
node_memory_MemAvailable_bytes
```

### Disk

```
node_disk_read_bytes_total
```

### Network

```
node_network_receive_bytes_total
```

---

# 🔴 9. Troubleshooting – Most Common in kubeadm

## 1. Check Grafana Logs

```bash
kubectl logs deploy/grafana -n monitoring
```

---

## 2. Test Prometheus Connectivity from Grafana Pod

```bash
kubectl exec -it deploy/grafana -n monitoring -- sh
curl http://prometheus:9090
```

---

## 3. Check Node Exporter

```bash
curl http://<node-ip>:9100/metrics
```

---

# 🚀 Next Level (I Will Help You)

We can now add:

* ✅ CPU alert > 80%
* ✅ Memory alert > 75%
* ✅ Disk alert
* ✅ Telegram / Email alert
* ✅ Monitor Kubernetes pods also

---

## Roshan tell me 3 things:

1. How many nodes in your kubeadm cluster?
2. Single master or multi master?
3. Want alerts on:

   * Email
   * Telegram
   * WhatsApp?

I will design exact production alerting YAML for you 😄
