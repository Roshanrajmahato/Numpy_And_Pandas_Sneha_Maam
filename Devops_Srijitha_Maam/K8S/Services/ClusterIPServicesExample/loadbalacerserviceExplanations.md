[Ingress + DNS in Kubernetes](https://chatgpt.com/share/6a1a8b82-bc1c-8321-a09b-fd97e61d5720)
# How Cloud Load Balancer Gets Created in Kubernetes

You do NOT manually attach the cloud load balancer.

Kubernetes automatically creates and attaches it when:

```yaml
type: LoadBalancer
```

is used in the Service file.

---

# Complete Flow

```text
Your YAML
   ↓
Kubernetes API Server
   ↓
Cloud Controller Manager
   ↓
AWS / Azure / GCP API
   ↓
Cloud Load Balancer Created
   ↓
Connected to Kubernetes Service
   ↓
Traffic sent to Pods
```

---

# Example on AWS EKS

When you apply:

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

Kubernetes automatically:

1. Calls AWS API
2. Creates ELB/NLB
3. Attaches worker nodes
4. Routes traffic to pods

---

# Apply Service

```bash
kubectl apply -f frontend-service.yaml
```

---

# Check Service

```bash
kubectl get svc
```

Example output:

```text
NAME                TYPE           CLUSTER-IP      EXTERNAL-IP
frontend-service    LoadBalancer   10.96.10.20    a1b2c3.elb.amazonaws.com
```

---

# What Actually Happens Internally

## Step 1 — Service Created

```text
frontend-service
type = LoadBalancer
```

---

## Step 2 — Cloud Controller Detects It

Cloud Controller Manager watches services.

It sees:

```text
type: LoadBalancer
```

---

## Step 3 — Cloud Provider Creates LB

AWS creates:

* Classic ELB
  OR
* Network Load Balancer (NLB)

Azure creates:

* Azure Load Balancer

GCP creates:

* Google Cloud Load Balancer

---

## Step 4 — LB Attached to Worker Nodes

```text
Internet
   ↓
AWS Load Balancer
   ↓
Worker Node EC2
   ↓
NodePort
   ↓
Pods
```

---

# VERY IMPORTANT

`LoadBalancer` internally creates:

```text
LoadBalancer
    ↓
NodePort
    ↓
ClusterIP
```

So even if you don’t define NodePort,
Kubernetes automatically creates it internally.

---

# How to See NodePort

```bash
kubectl get svc
```

Example:

```text
NAME                TYPE           PORT(S)
frontend-service    LoadBalancer   80:32451/TCP
```

Here:

* `80` = service port
* `32451` = auto-created NodePort

---

# On Local Kubernetes (Minikube / Kind)

Cloud LB will NOT work automatically because:

* No AWS
* No Azure
* No GCP

You need:

* MetalLB
  OR
* Minikube tunnel

---

# Minikube Example

Start tunnel:

```bash
minikube tunnel
```

Then:

```bash
kubectl get svc
```

You’ll get external IP.

---

# Interview Explanation

> "In Kubernetes, when we create a Service with type LoadBalancer, Kubernetes communicates with the cloud provider using the Cloud Controller Manager. The cloud provider automatically provisions a cloud load balancer and connects it to the Kubernetes service and worker nodes."


# How to Access LoadBalancer Service

After creating:

```yaml id="k3fx0x"
type: LoadBalancer
```

Kubernetes creates:

```text id="rk07wg"
External Load Balancer URL/IP
```

---

# Step 1 — Check External IP

Run:

```bash id="3u5h6f"
kubectl get svc
```

Example:

```text id="0uzvyu"
NAME                TYPE           EXTERNAL-IP
frontend-service    LoadBalancer   a1b2c3.elb.amazonaws.com
```

---

# Step 2 — Access Application

Open browser:

```text id="2lgx2g"
http://a1b2c3.elb.amazonaws.com
```

Now traffic flow becomes:

```text id="9a6h8m"
Browser
   ↓
AWS Load Balancer DNS
   ↓
Kubernetes Service
   ↓
Frontend Pods
```

---

# Problem

Cloud providers give random DNS names like:

```text id="w0r5wt"
a1b2c3.elb.amazonaws.com
```

Instead, we usually want:

```text id="wlm19j"
www.myapp.com
```

OR

```text id="tdllfh"
app.mycompany.com
```

---

# How to Use Your Own Domain (DNS)

You need 3 things:

| Component         | Purpose                      |
| ----------------- | ---------------------------- |
| Domain Name       | myapp.com                    |
| DNS Provider      | Route53, GoDaddy, Cloudflare |
| Load Balancer DNS | Points domain to Kubernetes  |

---

# Complete Real Architecture

```text id="g7dq59"
User
 ↓
myapp.com
 ↓
DNS Record
 ↓
AWS Load Balancer
 ↓
Kubernetes Service
 ↓
Pods
```

---

# Option 1 — Using Route53 (AWS)

If domain is managed in AWS Route53.

---

## Create A Record / Alias

Point:

```text id="g8gt48"
myapp.com
```

TO:

```text id="22q3x5"
a1b2c3.elb.amazonaws.com
```

---

# Option 2 — Using GoDaddy / Cloudflare

Create:

## CNAME Record

| Type  | Name | Value                    |
| ----- | ---- | ------------------------ |
| CNAME | www  | a1b2c3.elb.amazonaws.com |

---

# Example

```text id="m5v5fc"
www.myapp.com
        ↓
a1b2c3.elb.amazonaws.com
```

Now access:

```text id="4zjlwm"
http://www.myapp.com
```

---

# For Root Domain

Example:

```text id="mtk9yf"
myapp.com
```

Use:

* ALIAS record
  OR
* ANAME record
  OR
* Route53 Alias

because root domains cannot always use CNAME.

---

# Best Production Method → Ingress + DNS

Instead of exposing every app using separate LoadBalancers:

Use:

* One LoadBalancer
* One Ingress Controller
* Multiple Domains

---

# Example

```text id="nbb3qy"
api.myapp.com      → backend
shop.myapp.com     → ecommerce
admin.myapp.com    → admin panel
```

All handled by one Ingress.

---

# Ingress Example

```yaml id="6l9l4q"
apiVersion: networking.k8s.io/v1
kind: Ingress

metadata:
  name: app-ingress

spec:
  rules:
    - host: myapp.com

      http:
        paths:
          - path: /

            pathType: Prefix

            backend:
              service:
                name: frontend-service

                port:
                  number: 80
```

---

# Then Point DNS To Ingress LoadBalancer

```text id="jv5iw2"
myapp.com
    ↓
Ingress LoadBalancer
```

---

# HTTPS / SSL

Usually we add:

* TLS certificate
* HTTPS

Using:

* Cert Manager
* Let’s Encrypt
* AWS ACM

---

# Production Architecture

```text id="a5bwhv"
Internet
   ↓
Route53 / Cloudflare DNS
   ↓
AWS Load Balancer
   ↓
Ingress Controller
   ↓
Kubernetes Services
   ↓
Pods
```

---

# Interview Explanation

> "To access a Kubernetes LoadBalancer service, we use the external IP or DNS generated by the cloud provider. For custom domains, we create DNS records in providers like Route53 or Cloudflare and point them to the load balancer DNS. In production, Ingress is commonly used with a single load balancer to manage multiple domains and routes."


