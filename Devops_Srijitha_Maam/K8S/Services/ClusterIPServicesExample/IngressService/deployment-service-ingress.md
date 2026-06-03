[Ingress + DNS in Kubernetes](https://chatgpt.com/share/6a1a8b82-bc1c-8321-a09b-fd97e61d5720)
[Ingress files Explanations](https://chatgpt.com/share/6a1a922a-18d0-8320-ab1d-1f172e4752a9)
# Complete Setup of Ingress + DNS in Kubernetes

This is the real production setup used in companies.

---

# Final Architecture

```text id="m6f96t"
Internet
   ↓
DNS (Route53 / Cloudflare/ Go-Daddy)
   ↓
Load Balancer
   ↓
Ingress Controller
   ↓
Ingress Rules
   ↓
Kubernetes Service
   ↓
Pods
```

---

# What Changes You Need

You currently have:

```yaml id="05xkrq"
type: NodePort
```

OR

```yaml id="5fx5uj"
type: LoadBalancer
```

For Ingress setup:

✅ Change service type to:

```yaml id="qefyq1"
type: ClusterIP
```

because Ingress will handle external traffic.

---

# STEP 1 — Frontend Deployment

Example:

```yaml id="5zawif"
apiVersion: apps/v1
kind: Deployment

metadata:
  name: frontend-deployment

spec:
  replicas: 2

  selector:
    matchLabels:
      app: frontend

  template:
    metadata:
      labels:
        app: frontend

    spec:
      containers:
        - name: frontend
          image: nginx

          ports:
            - containerPort: 80
```

---

# STEP 2 — Change Service to ClusterIP

```yaml id="zfx3h0"
apiVersion: v1
kind: Service

metadata:
  name: frontend-service

spec:
  type: ClusterIP

  selector:
    app: frontend

  ports:
    - port: 80
      targetPort: 80
```

---

# Why ClusterIP?

Because:

```text id="nq1e7j"
Ingress
   ↓
Service
   ↓
Pods
```

Ingress internally talks to services.

---

# STEP 3 — Install NGINX Ingress Controller

On cloud cluster:

```bash id="kvq0m8"
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

---

# What Happens?

Kubernetes creates:

```text id="3g6fjm"
NGINX Ingress Controller
```

AND automatically creates:

```text id="fhw1e5"
LoadBalancer Service
```

---

# Check It

```bash id="svtjlwm"
kubectl get svc -n ingress-nginx
```

Example:

```text id="4nmqix"
NAME                                 TYPE           EXTERNAL-IP
ingress-nginx-controller             LoadBalancer   a1b2c3.elb.amazonaws.com
```

THIS becomes your public entry point.

---

# STEP 4 — Create Ingress Resource

```yaml id="6f1j2z"
apiVersion: networking.k8s.io/v1
kind: Ingress

metadata:
  name: frontend-ingress

spec:
  ingressClassName: nginx

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

# Apply Files

```bash id="61av9p"
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service-clusterip.yaml
kubectl apply -f frontend-ingress-nginx.yaml
```

---

# STEP 5 — Configure DNS

Now take:

```text id="ygtj7j"
a1b2c3.elb.amazonaws.com
```

from:

```bash id="xj7jq3"
kubectl get svc -n ingress-nginx
```

---

# In Cloudflare / Route53 / GoDaddy

Create DNS Record:

| Type  | Name | Value                    |
| ----- | ---- | ------------------------ |
| CNAME | www  | a1b2c3.elb.amazonaws.com |

OR

| Type      | Name      | Value |
| --------- | --------- | ----- |
| A / Alias | myapp.com | ELB   |

---

# Final Traffic Flow

```text id="0l0j3l"
User
 ↓
myapp.com
 ↓
DNS
 ↓
AWS Load Balancer
 ↓
NGINX Ingress Controller
 ↓
Ingress Rule
 ↓
frontend-service
 ↓
Frontend Pods
```

---

# Multiple Apps Example

One Ingress can manage many apps:

```yaml id="w5b5lu"
rules:
  - host: api.myapp.com
    backend: backend-service

  - host: shop.myapp.com
    backend: ecommerce-service
```

---

# HTTPS Setup (Production)

Usually add:

* TLS
* SSL Certificate

Using:

* Cert Manager
* Let’s Encrypt
* AWS ACM

---

# Check Ingress

```bash id="w3mofw"
kubectl get ingress
```

---

# Interview Explanation

> "In production Kubernetes, we usually expose applications using Ingress instead of multiple LoadBalancers. We install an Ingress Controller like NGINX, create Ingress rules for domain routing, and point DNS records to the Ingress LoadBalancer. Services remain internal using ClusterIP."
