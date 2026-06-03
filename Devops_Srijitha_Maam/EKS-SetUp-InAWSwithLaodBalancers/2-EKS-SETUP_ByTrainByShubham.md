[EASIEST EKS Cluster Setup & Deployment of Two-Tier Application ](https://youtu.be/6ZALmrssgfc?si=8gLYpnFRVmu7oZWc)


# ☁️ 🟠 AWS EKS Complete Setup Guide

## 🎯 Goal

Create a Kubernetes Cluster on AWS EKS and deploy your application with a public AWS Load Balancer.

```text
👨‍💻 DevOps Engineer
        │
        ▼
🟠 AWS IAM
        │
        ▼
🖥️ EC2 Bastion Host
        │
        ▼
☸️ EKS Cluster
        │
        ▼
📦 Kubernetes Workloads
        │
        ▼
🌐 AWS Load Balancer
        │
        ▼
👥 End Users
```

---

# 🟠 Phase 1: IAM User Setup

### Why?

IAM User provides secure AWS API access for creating EKS resources.

### AWS Console

```text
AWS Console
   ↓
IAM
   ↓
Users
   ↓
Create User
```

### User Name

```text
eks-admin
```

### Permission

```text
AdministratorAccess
```

### Create Access Keys

```text
IAM
 ↓
Users
 ↓
eks-admin
 ↓
Security Credentials
 ↓
Create Access Key
```

### Save

```text
🔑 Access Key ID
🔐 Secret Access Key
```

These credentials will be used by AWS CLI.

---

# 🖥️ Phase 2: Create EC2 Instance

### Why?

Acts as a **Bastion Host / Management Server** from where we manage Kubernetes.

### Configuration

| Setting     | Value        |
| ----------- | ------------ |
| 🌎 Region   | us-west-2    |
| 🐧 OS       | Ubuntu 22.04 |
| 💻 Instance | t2.medium    |
| 💾 Storage  | 30 GB        |

### Security Group

```text
SSH   → 22
HTTP  → 80
HTTPS → 443
```

### Connect

```bash
ssh -i eks.pem ubuntu@<PUBLIC-IP>
```

---

# ☁️ Phase 3: Install AWS CLI

### Why?

AWS CLI allows the server to communicate with AWS services.

### Commands

```bash
sudo apt update

sudo apt install unzip -y

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip

unzip awscliv2.zip

sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin --update

aws --version
```

### Configure AWS Account

```bash
aws configure
```

Provide:

```text
Access Key ID
Secret Access Key
us-west-2
json
```

### Verify

```bash
aws sts get-caller-identity
```

✅ Confirms AWS CLI authentication.

---

# 🐳 Phase 4: Install Docker

### Why?

Docker runs containerized applications.

Without Docker:

```text
Pod ❌
Container ❌
Image ❌
```

### Commands

```bash
sudo apt update

sudo apt install docker.io -y

sudo systemctl enable docker

sudo systemctl start docker

sudo chown $USER /var/run/docker.sock

newgrp docker

docker ps
```

### Verify

```bash
docker ps
```

✅ Docker Engine Running

---

# ☸️ Phase 5: Install kubectl

### Why?

kubectl is used to communicate with Kubernetes Cluster.

```text
kubectl
   │
   ▼
Kubernetes API Server
   │
   ▼
Cluster
```

### Commands

```bash
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubectl

chmod +x kubectl

sudo mv kubectl /usr/local/bin

kubectl version --client
```

---

# 🚀 Phase 6: Install eksctl

### Why?

eksctl automates EKS cluster creation.

Without eksctl:

```text
VPC
Subnets
Route Tables
Security Groups
Node Groups
EKS Cluster

Create Everything Manually 😭
```

With eksctl:

```bash
eksctl create cluster
```

### Commands

```bash
curl --silent --location \
"https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" \
| tar xz -C /tmp

sudo mv /tmp/eksctl /usr/local/bin

eksctl version
```

---

# ☸️ Phase 7: Create EKS Cluster

### Why?

EKS provides a managed Kubernetes Control Plane.

### Command

```bash
eksctl create cluster \
--name three-tier-cluster \
--region us-west-2 \
--node-type t2.medium \
--nodes-min 2 \
--nodes-max 2
```

### What AWS Creates

```text
☸️ EKS Control Plane
🌐 VPC
🛣️ Route Tables
🔒 Security Groups
📡 Subnets
🖥️ 2 Worker Nodes
📈 Auto Scaling Group
```

### Verify

```bash
aws eks update-kubeconfig \
--region us-west-2 \
--name three-tier-cluster

kubectl get nodes
```

Expected:

```text
STATUS
Ready
Ready
```

---

# 📂 Phase 8: Create Namespace

### Why?

Namespaces logically separate applications.

### Command

```bash
kubectl create namespace two-tier-ns
```

### Verify

```bash
kubectl get ns
```

---

# 📦 Phase 9: Deploy Application

### Why?

Deploy frontend, backend and database workloads.

### Deploy

```bash
kubectl apply -f .
```

### Verify

```bash
kubectl get all -A
```

---

# 🌐 Phase 10: Install AWS Load Balancer Controller

### Why?

Kubernetes cannot create AWS Load Balancers by itself.

AWS Load Balancer Controller acts as a bridge.

```text
Kubernetes Service
         │
         ▼
AWS Load Balancer Controller
         │
         ▼
AWS Load Balancer
```

---

## Step 1: Create IAM Policy

```bash
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json

aws iam create-policy \
--policy-name AWSLoadBalancerControllerIAMPolicy \
--policy-document file://iam_policy.json
```

### Why?

Provides permissions to create:

```text
ALB
NLB
Target Groups
Listeners
Security Groups
```

---

## Step 2: Associate OIDC

```bash
eksctl utils associate-iam-oidc-provider \
--region us-west-2 \
--cluster three-tier-cluster \
--approve
```

### Why?

Allows Pods to securely access AWS services.

```text
Pod
 ↓
IAM Role
 ↓
AWS Service
```

---

## Step 3: Create Service Account

```bash
eksctl create iamserviceaccount \
--cluster=three-tier-cluster \
--namespace=kube-system \
--name=aws-load-balancer-controller \
--role-name=AmazonEKSLoadBalancerControllerRole \
--attach-policy-arn=arn:aws:iam::<ACCOUNT_ID>:policy/AWSLoadBalancerControllerIAMPolicy \
--approve \
--region=us-west-2
```

### Why?

Gives AWS permissions to the Controller Pod.

---

# ⛵ Phase 11: Install Helm

### Why?

Helm is Kubernetes Package Manager.

```text
Linux → apt
Python → pip
NodeJS → npm
Kubernetes → helm
```

### Command

```bash
sudo snap install helm --classic
```

Verify

```bash
helm version
```

---

# ⚙️ Phase 12: Install AWS Load Balancer Controller

### Commands

```bash
helm repo add eks https://aws.github.io/eks-charts

helm repo update

helm install aws-load-balancer-controller \
eks/aws-load-balancer-controller \
-n kube-system \
--set clusterName=three-tier-cluster \
--set serviceAccount.create=false \
--set serviceAccount.name=aws-load-balancer-controller
```

### Verify

```bash
kubectl get deployment -n kube-system aws-load-balancer-controller
```

Expected

```text
AVAILABLE
2
```

---

# 🌎 Phase 13: Create Public Load Balancer

### Why?

Expose application to internet.

### Service Manifest

```yaml
type: LoadBalancer
```

### Deploy

```bash
kubectl apply -f full_stack_lb.yaml
```

### Verify

```bash
kubectl get svc
```

Output

```text
frontend-service
LoadBalancer
a1b2c3.us-west-2.elb.amazonaws.com
```

---

# 🎯 Complete Traffic Flow

```text
👥 Users
   │
   ▼
🌎 Internet
   │
   ▼
⚖️ AWS Load Balancer
   │
   ▼
📦 Frontend Service
   │
   ▼
🖥️ Frontend Pods
   │
   ▼
📦 Backend Service (ClusterIP)
   │
   ▼
⚙️ Backend Pods
   │
   ▼
📦 Database Service (ClusterIP)
   │
   ▼
🗄️ Database
```

---

# 🔍 Useful Verification Commands

### Cluster

```bash
kubectl get nodes
```

### Pods

```bash
kubectl get pods -A
```

### Services

```bash
kubectl get svc -A
```

### Deployments

```bash
kubectl get deployments -A
```

### Namespaces

```bash
kubectl get ns
```

### Cluster Information

```bash
kubectl cluster-info
```

---

# 🧹 Cleanup (Important)

### Delete Application

```bash
kubectl delete -f .
```

### Delete Cluster

```bash
eksctl delete cluster \
--name three-tier-cluster \
--region us-west-2
```

### Why?

AWS resources continue billing until deleted.

```text
☸️ EKS Cluster
🖥️ Worker Nodes
⚖️ Load Balancer
💾 EBS Volumes
```

Deleting the cluster removes all associated infrastructure and stops charges.


# ☁️ AWS EKS + ALB Ingress Complete Flow

After creating the EKS cluster and installing the AWS Load Balancer Controller, you can expose your application using **Ingress + ALB** instead of a Service of type `LoadBalancer`.

---

# 🌐 Why Use Ingress?

### Without Ingress

```text
Frontend Service (LoadBalancer)
Backend Service (LoadBalancer)
Admin Service (LoadBalancer)
```

Result:

```text
❌ 3 AWS Load Balancers
❌ Higher Cost
❌ Harder Management
```

---

### With Ingress

```text
1 AWS ALB
       │
       ├── / → Frontend
       │
       ├── /api → Backend
       │
       └── /admin → Admin
```

Result:

```text
✅ Single ALB
✅ Lower Cost
✅ Easier Routing
```

---

# 🟠 Step 1: Create IAM Policy

```bash
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json

aws iam create-policy \
--policy-name AWSLoadBalancerControllerIAMPolicy \
--policy-document file://iam_policy.json
```

---

# 🟠 Step 2: Associate OIDC Provider

```bash
eksctl utils associate-iam-oidc-provider \
--region us-west-2 \
--cluster three-tier-cluster \
--approve
```

### Why?

```text
Pod
 ↓
IAM Role
 ↓
AWS APIs
```

Allows Kubernetes Pods to securely access AWS services.

---

# 🟠 Step 3: Create IAM Role

Example Role:

```text
eks-alb-role
```

Attach:

```text
AWSLoadBalancerControllerIAMPolicy
```

---

# 🟠 Step 4: Create ServiceAccount

### aws-load-balancer-controller-sa.yaml

```yaml
apiVersion: v1
kind: ServiceAccount

metadata:
  name: aws-load-balancer-controller
  namespace: kube-system

  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::936379345511:role/eks-alb-role
```

Apply:

```bash
kubectl apply -f aws-load-balancer-controller-sa.yaml
```

Verify:

```bash
kubectl get sa -n kube-system
```

---

# ⛵ Step 5: Install Helm

```bash
sudo snap install helm --classic
```

Verify:

```bash
helm version
```

---

# ⚙️ Step 6: Install AWS Load Balancer Controller

Add Repository:

```bash
helm repo add eks https://aws.github.io/eks-charts

helm repo update
```

Install Controller:

```bash
helm install aws-load-balancer-controller \
eks/aws-load-balancer-controller \
-n kube-system \
--set clusterName=three-tier-cluster \
--set serviceAccount.create=false \
--set serviceAccount.name=aws-load-balancer-controller
```

Verify:

```bash
kubectl get deployment -n kube-system aws-load-balancer-controller
```

Expected:

```text
AVAILABLE
2
```

---

# 📦 Step 7: Deploy Application

```bash
kubectl apply -f .
```

Verify:

```bash
kubectl get all -A
```

---

# 📦 Step 8: Services Must Be ClusterIP

### frontend-service.yaml

```yaml
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

### backend-service.yaml

```yaml
apiVersion: v1
kind: Service

metadata:
  name: backend-service

spec:
  type: ClusterIP

  selector:
    app: backend

  ports:
  - port: 5000
    targetPort: 5000
```

---

# 🌐 Step 9: Create Ingress

### ingress.yaml

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress

metadata:
  name: three-tier-ingress

  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip

spec:
  ingressClassName: alb

  rules:
  - http:

      paths:

      - path: /
        pathType: Prefix

        backend:
          service:
            name: frontend-service

            port:
              number: 80

      - path: /api
        pathType: Prefix

        backend:
          service:
            name: backend-service

            port:
              number: 5000
```

Apply:

```bash
kubectl apply -f ingress.yaml
```

---

# 🔍 Step 10: Verify Ingress

```bash
kubectl get ingress
```

Output:

```text
NAME                  CLASS   HOSTS   ADDRESS
three-tier-ingress    alb     *       k8s-default-xxxxx.elb.amazonaws.com
```

---

# 🌎 Traffic Flow

```text
👥 Users
    │
    ▼
🌐 Internet
    │
    ▼
⚖️ AWS ALB
    │
    ├────────────► /
    │              │
    │              ▼
    │        Frontend Service
    │              │
    │              ▼
    │        Frontend Pods
    │
    └────────────► /api
                   │
                   ▼
            Backend Service
                   │
                   ▼
              Backend Pods
```

---

# 🔍 Useful Verification Commands

### Nodes

```bash
kubectl get nodes
```

### Pods

```bash
kubectl get pods -A
```

### Services

```bash
kubectl get svc -A
```

### Ingress

```bash
kubectl get ingress
```

### Controller

```bash
kubectl get deployment -n kube-system aws-load-balancer-controller
```

### Namespace

```bash
kubectl get ns
```

---

# 🧹 Delete Application

```bash
kubectl delete -f .
```

Delete Ingress:

```bash
kubectl delete ingress three-tier-ingress
```

Delete Load Balancer Controller:

```bash
helm uninstall aws-load-balancer-controller -n kube-system
```

---

# ☠️ Delete Entire EKS Cluster

This removes:

```text
☸️ EKS Control Plane
🖥️ Worker Nodes
🌐 VPC Components Created by eksctl
⚖️ ALB/NLB
💾 EBS Volumes Attached to Nodes
🔒 Security Groups
📡 Subnets Created by eksctl
```

Command:

```bash
eksctl delete cluster \
--name three-tier-cluster \
--region us-west-2
```

Verify:

```bash
aws eks list-clusters
```

If the cluster is deleted successfully:

```text
{
  "clusters": []
}
```

---

# 🎯 Real Production Architecture

```text
                    👥 Users
                        │
                        ▼
                  🌎 Internet
                        │
                        ▼
              ⚖️ AWS ALB (Ingress)
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
   Frontend Service              Backend Service
    (ClusterIP)                   (ClusterIP)
        │                               │
        ▼                               ▼
   Frontend Pods                  Backend Pods
                                          │
                                          ▼
                                   Database Service
                                     (ClusterIP)
                                          │
                                          ▼
                                      RDS / DB
```

This is the architecture most teams use in production: **ALB Ingress → ClusterIP Services → Pods**, rather than exposing every service with its own `LoadBalancer`.


