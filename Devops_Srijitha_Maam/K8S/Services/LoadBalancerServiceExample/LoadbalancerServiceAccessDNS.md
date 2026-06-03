# Accessing LoadBalancer IP and Attaching DNS

You currently have:

```text id="fjlwm1"
Internet
   ↓
LoadBalancer Service
   ↓
Frontend Pods
```

Now you want:

1. Access LoadBalancer IP
2. Attach custom DNS/domain name

This is REAL production Kubernetes architecture.

---

# STEP 1 — Your LoadBalancer Service

Example:

```yaml id="rjlwm2"
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

# STEP 2 — Apply Service

```bash id="pjlwm3"
kubectl apply -f frontend-service.yaml
```

---

# STEP 3 — Check Service

Run:

```bash id="njlwm4"
kubectl get svc
```

Example output:

```text id="ljlwm5"
NAME               TYPE           CLUSTER-IP      EXTERNAL-IP
frontend-service   LoadBalancer   10.96.12.20    a1b2c3d4.elb.amazonaws.com
```

---

# MOST IMPORTANT

# EXTERNAL-IP

This is your cloud Load Balancer address.

Example:

```text id="jjlwm6"
a1b2c3d4.elb.amazonaws.com
```

OR sometimes IP:

```text id="hjlwm7"
35.200.10.20
```

---

# STEP 4 — Access Application

Open browser:

```text id="fjlwm8"
http://a1b2c3d4.elb.amazonaws.com
```

OR

```text id="djlwm9"
http://35.200.10.20
```

Now traffic flow:

```text id="bjlwm0"
Browser
   ↓
Cloud Load Balancer
   ↓
frontend-service
   ↓
Frontend Pods
```

---

# IMPORTANT AWS UNDERSTANDING

In AWS:

Kubernetes automatically creates:

* ELB
* NLB
* ALB

depending on configuration.

---

# How LoadBalancer Internally Works

```text id="9jlw11"
Internet
    ↓
AWS ELB
    ↓
NodePort (internally)
    ↓
ClusterIP Service
    ↓
Pods
```

VERY IMPORTANT:

LoadBalancer internally uses:

* NodePort
* ClusterIP

---

# STEP 5 — Attach Custom Domain

Suppose domain:

```text id="7jlw12"
myapp.com
```

purchased from:

* GoDaddy
* Namecheap
* Route53
* Cloudflare

---

# DNS ATTACHMENT PROCESS

```text id="5jlw13"
Domain
   ↓
DNS Record
   ↓
LoadBalancer Address
```

---

# OPTION 1 — Using AWS Route53

BEST production method.

---

# Create Hosted Zone

In:

Amazon Web Services

Go to:

```text id="3jlw14"
Route53
```

Create:

* Hosted Zone
* Domain records

---

# Create A Record

Example:

```text id="1jlw15"
Type: A
Name: app
Value: LoadBalancer DNS/IP
```

---

# Result

```text id="zjlw16"
app.myapp.com
      ↓
LoadBalancer
```

---

# OPTION 2 — Using Cloudflare

If using:

Cloudflare

Go to DNS section.

Add:

| Type  | Name | Value            |
| ----- | ---- | ---------------- |
| CNAME | app  | LoadBalancer DNS |

Example:

```text id="xjlw17"
app → a1b2c3d4.elb.amazonaws.com
```

---

# FINAL FLOW

```text id="vjlw18"
app.myapp.com
      ↓
DNS Resolution
      ↓
AWS LoadBalancer
      ↓
frontend-service
      ↓
frontend Pods
```

---

# REAL PRODUCTION BEST PRACTICE

Normally we do NOT expose Services directly.

Instead we use:

```text id="tjlw19"
Ingress Controller
```

Architecture:

```text id="rjlw20"
Internet
   ↓
DNS
   ↓
Ingress LoadBalancer
   ↓
Ingress Rules
   ↓
Frontend Service
   ↓
Frontend Pods
```

---

# Why Ingress Better?

Because:

* one LoadBalancer for many apps
* path routing
* domain routing
* SSL support
* cheaper
* production standard

---

# Example Real Production

```text id="pjlw21"
app.myapp.com
api.myapp.com
admin.myapp.com
```

all handled by ONE Ingress LoadBalancer.

---

# Important Command

Check external IP:

```bash id="ojlw22"
kubectl get svc frontend-service
```

---

# If EXTERNAL-IP Shows <pending>

Means:

* cloud LoadBalancer still creating
* OR no cloud integration exists

---

# IMPORTANT REALITY

# LoadBalancer Works Properly On:

✅ AWS EKS
✅ GKE
✅ AKS
✅ DigitalOcean Kubernetes

---

# For Local Kubernetes

Examples:

* Minikube
* Kind
* kubeadm local VM

`LoadBalancer` may stay:

```text id="njlw23"
<pending>
```

because no cloud provider exists.

---

# For kubeadm on AWS EC2

You need:

* AWS Cloud Controller Manager
  OR
* MetalLB

to get external LoadBalancer.

---

# Real Traffic Journey

```text id="mjlw24"
User Browser
      ↓
DNS lookup
      ↓
LoadBalancer IP/DNS
      ↓
AWS ELB
      ↓
Kubernetes Service
      ↓
Frontend Pods
```

---

# Final Most Important Understanding

# LoadBalancer Service

Creates:

* external access point
* cloud load balancer
* public endpoint

---

# DNS

Maps:

* human-friendly name
  → LoadBalancer address

Example:

```text id="ljlw25"
app.mycompany.com
      ↓
a1b2c3d4.elb.amazonaws.com
```
