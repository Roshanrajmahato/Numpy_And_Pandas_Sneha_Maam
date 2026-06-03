# **Create Namespace if It Does Not Exist**

```bash
kubectl create namespace services
```

**What it does:**
Directly creates a namespace without YAML.

### **Verify Namespace Creation**

```bash
kubectl get namespaces
```

2️⃣ Create deploymentservices.yaml

### Create the Pod

```bash
kubectl create -f deploymentservices.yaml
```

>runcmd
       > ` kubectl get deployments -n services  `
       > ` kubectl get pods -n services `
       > ` kubectl get rs -n services `


To Get The Pods 
```bash
kubectl get pods -o wide

# To Get The Pods with namspace (configmaps)
kubectl get pods -n services -o wide

``````bash

2️⃣ Create NodePortService.yaml

>runcmd
       > ` kubectl create -f NodePortService.yaml  `

2️⃣ Create LoadBalancerService.yaml

>runcmd
       > ` kubectl create -f LoadBalancerService.yaml  `

## services Management Commands

### List services

```bash
kubectl get services
```

---

### Describe a ConfigMap

```bash
kubectl describe services <name>
```