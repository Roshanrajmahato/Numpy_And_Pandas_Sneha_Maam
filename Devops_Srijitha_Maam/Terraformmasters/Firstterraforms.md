# Terraform Create EC2 Instance on AWS — Complete Interview Notes


## What is Terraform?

HashiCorp Terraform is an **Infrastructure as Code (IaC)** tool used to create, manage, and automate infrastructure using code instead of manually creating resources from the cloud console.

With Terraform, you can automate:

* EC2 Instances
* VPC
* Security Groups
* Load Balancers
* S3 Buckets
* Databases
* Kubernetes Clusters

Terraform supports many cloud providers:

* Amazon Web Services AWS
* Google Cloud GCP
* Microsoft Azure Azure

---

# Why Terraform is Popular

## Advantages

### 1. Infrastructure as Code (IaC)

Everything is written in code.

Benefits:

* Reusable
* Version controlled
* Easy automation
* Easy collaboration

---

### 2. Multi-Cloud Support

One tool can manage:

* AWS
* Azure
* GCP

---

### 3. Declarative Language

You only describe:

> “What infrastructure you want”

Terraform decides:

> “How to create it”

---

### 4. State Management

Terraform stores infrastructure details in:

```bash
terraform.tfstate
```

This helps Terraform track:

* Created resources
* Changes
* Deletions

---

# Important Terraform Interview Definition

## What is IaC?

Infrastructure as Code means managing infrastructure using configuration files instead of manual setup.

---

# Terraform Workflow

```text
Write Code → Init → Plan → Apply → Infrastructure Created
```

---

# Prerequisites

Before creating EC2:

## Install Terraform

Download from:

[Terraform Official Website](https://developer.hashicorp.com/terraform?utm_source=chatgpt.com)

Check version:

```bash
terraform -version
```

---

# Step 1 — Create AWS Account

Go to:

[AWS Official Website](https://aws.amazon.com/?utm_source=chatgpt.com)

Create:

* Free Tier account

---

# Step 2 — Generate AWS Access Keys

Terraform needs AWS credentials to communicate with AWS APIs.

## Generate:

* Access Key ID
* Secret Access Key

Path:

```text
AWS Console → Security Credentials → Access Keys
```

---

# Interview Question

## Why do we need Access Keys?

Terraform communicates with AWS programmatically using AWS APIs.

Access keys provide authentication.

---

# Step 3 — Create Terraform File

Terraform files use:

```text
.tf extension
```

Example:

```text
main.tf
```

---

# Terraform Basic Structure

```hcl
provider "aws" {

}

resource "aws_instance" "example" {

}
```

---

# Understanding Provider Block

## Provider

Provider tells Terraform:

> Which cloud platform should be used.

Example:

```hcl
provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAUOB6V533PJWDFQ7T"
  secret_key = "V6gBgRleNvnLMYar6X3rflFpa0uTZuMkedm9z17I"
}
```

---

# Interview Explanation

## What is Provider in Terraform?

Provider is a plugin that allows Terraform to interact with APIs of cloud providers.

Examples:

* AWS Provider
* Azure Provider
* Google Provider

---

# Understanding Resource Block

## Resource

A resource is:

> Any infrastructure component Terraform creates.

Examples:

* EC2
* S3
* VPC
* Security Group

---

# EC2 Instance Terraform Code

```hcl
provider "aws" {
  region     = "eu-central-1"
  access_key = "YOUR_ACCESS_KEY"
  secret_key = "YOUR_SECRET_KEY"
}

resource "aws_instance" "ec2_example" {

  ami           = "ami-0767046d1677be5a0"
  instance_type = "t2.micro"

  tags = {
    Name = "Terraform EC2"
  }
}
```

---

# Code Explanation

## provider "aws"

Connects Terraform to AWS.

---

## region

AWS region where instance will launch.

Examples:

* us-east-1
* ap-south-1
* eu-central-1

---

## aws_instance

Terraform AWS EC2 resource.

---

## ami

Amazon Machine Image.

Defines:

* Operating System
* Preinstalled software

Examples:

* Ubuntu
* Amazon Linux
* CentOS

---

## instance_type

Defines:

* CPU
* RAM
* Pricing

Examples:

* t2.micro
* t2.small
* t3.medium

---

## tags

Used for naming and identifying resources.

---

# Interview Questions

## What is AMI?

AMI stands for:

> Amazon Machine Image

It is a template containing:

* Operating system
* Software configuration

Used to launch EC2 instances.

---

## What is Instance Type?

Defines hardware configuration:

* CPU
* Memory
* Network Performance

---

# How to Find AMI

Path:

```text
AWS Console → EC2 → AMIs
```

Search:

```text
Ubuntu
```

Copy:

```text
AMI ID
```

---

# Terraform Commands

# 1. terraform init

## Purpose

Initializes Terraform project.

Downloads:

* Providers
* Dependencies

Command:

```bash
terraform init
```

---

# Interview Question

## What does terraform init do?

* Downloads provider plugins
* Initializes backend
* Prepares working directory

---

# 2. terraform plan

## Purpose

Shows execution preview.

Terraform compares:

* Current infrastructure
* Desired infrastructure

Command:

```bash
terraform plan
```

---

# Important Concept

Terraform creates:

> Execution Plan

Shows:

* Resources to add
* Modify
* Destroy

---

# Interview Question

## Does terraform plan create infrastructure?

❌ No

It only shows preview.

---

# 3. terraform apply

## Purpose

Actually creates infrastructure.

Command:

```bash
terraform apply
```

Terraform asks:

```text
Enter a value: yes
```

Then creates EC2 instance.

---

# Interview Question

## What is terraform apply?

Used to provision infrastructure on cloud.

---

# 4. terraform destroy

## Purpose

Deletes all managed resources.

Command:

```bash
terraform destroy
```

---

# Interview Question

## Why terraform destroy?

Used to:

* Remove infrastructure
* Avoid cloud cost

---

# Terraform State File

## terraform.tfstate

Stores:

* Resource IDs
* Metadata
* Infrastructure mapping

---

# Interview Question

## Why is Terraform State important?

Terraform uses state to:

* Track resources
* Detect changes
* Update infrastructure efficiently

---

# Important Terraform Files

| File              | Purpose              |
| ----------------- | -------------------- |
| main.tf           | Main configuration   |
| variables.tf      | Input variables      |
| outputs.tf        | Output values        |
| terraform.tfstate | Infrastructure state |
| terraform.tfvars  | Variable values      |

---

# User Data in Terraform

## What is user_data?

Used to run startup scripts automatically when EC2 boots.

---

# Example

```hcl
resource "aws_instance" "ec2_example" {

  ami           = "ami-0767046d1677be5a0"
  instance_type = "t2.micro"

  user_data = <<-EOF
      #!/bin/bash
      apt update
      apt install -y apache2
      systemctl start apache2
  EOF
}
```

---

# What Happens Here?

When EC2 starts:

1. Updates packages
2. Installs Apache
3. Starts Apache server

Automatically.

---

# Interview Question

## Why use user_data?

Used for:

* Bootstrapping
* Initial server configuration
* Installing software automatically

---

# Security Group in Terraform

Security Groups act as:

> Virtual Firewall

Controls:

* Inbound traffic
* Outbound traffic

---

# Example Security Group

```hcl
resource "aws_security_group" "main" {

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

# Explanation

## ingress

Incoming traffic rules.

Example:

* SSH access on port 22

---

## egress

Outgoing traffic rules.

---

# Interview Question

## Difference between ingress and egress?

| Type    | Meaning          |
| ------- | ---------------- |
| Ingress | Incoming traffic |
| Egress  | Outgoing traffic |

---

# Terraform Provisioners

Provisioners execute commands on local or remote machines.

Types:

* file
* remote-exec
* local-exec

---

# file Provisioner

Copies file from local machine to remote server.

Example:

```hcl
provisioner "file" {
  source      = "startup.sh"
  destination = "/home/ubuntu/startup.sh"
}
```

---

# remote-exec Provisioner

Executes commands remotely.

Example:

```hcl
provisioner "remote-exec" {
  inline = [
    "chmod +x startup.sh",
    "./startup.sh"
  ]
}
```

---

# Connection Block

Used for SSH connection.

```hcl
connection {
  type        = "ssh"
  host        = self.public_ip
  user        = "ubuntu"
  private_key = file("aws_key")
}
```

---

# Interview Question

## Difference between user_data and provisioners?

| user_data            | Provisioner         |
| -------------------- | ------------------- |
| Runs during boot     | Runs after creation |
| Simple startup tasks | Complex automation  |
| Cloud-init based     | SSH based           |

---

# Terraform Lifecycle

```text
Write Code
↓
terraform init
↓
terraform plan
↓
terraform apply
↓
Infrastructure Created
↓
terraform destroy
```

---

# Best Practices

## 1. Never Hardcode Credentials

❌ Bad

```hcl
access_key = "XXXX"
```

✅ Good

Use:

* Environment variables
* IAM Roles
* AWS CLI profiles

---

# Environment Variable Method

```bash
export AWS_ACCESS_KEY_ID="XXXX"
export AWS_SECRET_ACCESS_KEY="XXXX"
```

---

# Interview Question

## Why avoid hardcoded credentials?

Security risk.

Credentials may leak through:

* GitHub
* Logs
* Shared files

---

# Important Terraform Interview Questions

# Basic Questions

## 1. What is Terraform?

Infrastructure as Code tool by HashiCorp.

---

## 2. What is Terraform State?

Tracks infrastructure resources.

---

## 3. Difference between terraform plan and apply?

| plan            | apply           |
| --------------- | --------------- |
| Preview changes | Execute changes |

---

## 4. What is Provider?

Plugin for cloud communication.

---

## 5. What is Resource?

Infrastructure object managed by Terraform.

---

# Intermediate Questions

## 6. What is user_data?

Startup script executed during EC2 boot.

---

## 7. What are Provisioners?

Used to execute scripts/commands.

---

## 8. Difference between mutable and immutable infrastructure?

| Mutable                | Immutable                 |
| ---------------------- | ------------------------- |
| Modify existing server | Replace server completely |

Terraform usually promotes immutable infrastructure.

---

## 9. What is idempotency?

Running same code multiple times gives same result.

Terraform is idempotent.

---

## 10. What is Terraform Drift?

When actual infrastructure differs from Terraform state/configuration.

---

# Advanced Interview Concepts

# Modules

Reusable Terraform code blocks.

Example:

* Reusable VPC module
* EC2 module

---

# Variables

Used for dynamic configuration.

Example:

```hcl
variable "instance_type" {
  default = "t2.micro"
}
```

Usage:

```hcl
instance_type = var.instance_type
```

---

# Outputs

Displays values after apply.

Example:

```hcl
output "public_ip" {
  value = aws_instance.ec2_example.public_ip
}
```

---

# Dependencies

Terraform automatically understands dependencies.

Example:

* EC2 depends on Security Group

---

# Real Project Interview Answer

## How Terraform Works Internally

1. Reads `.tf` files
2. Creates dependency graph
3. Checks current state
4. Creates execution plan
5. Applies infrastructure changes
6. Updates state file

---

# Real-Time Production Best Practices

## Use:

* Remote Backend (S3)
* State Locking (DynamoDB)
* Modules
* Variables
* Workspaces
* CI/CD pipelines

---

# Example Production Architecture

```text
Developer
   ↓
GitHub
   ↓
Jenkins/GitHub Actions
   ↓
Terraform
   ↓
AWS Infrastructure
```

---

# Terraform Advantages vs CloudFormation

| Terraform       | CloudFormation |
| --------------- | -------------- |
| Multi-cloud     | AWS only       |
| Easier syntax   | Verbose        |
| Large community | AWS native     |

---

# Most Important Interview Topics

Focus strongly on:

* Providers
* Resources
* State file
* Variables
* Outputs
* Modules
* Provisioners
* user_data
* terraform init/plan/apply/destroy
* Security Groups
* Remote backend
* Idempotency

---

# Quick Revision Notes

```text
terraform init     → Initialize project
terraform plan     → Preview changes
terraform apply    → Create infrastructure
terraform destroy  → Delete infrastructure
```

---

# One-Line Interview Answers

## Terraform

Infrastructure as Code tool used to automate cloud infrastructure.

---

## Provider

Plugin used to communicate with cloud providers.

---

## Resource

Infrastructure object managed by Terraform.

---

## State File

Tracks current infrastructure state.

---

## user_data

Startup script executed during EC2 launch.

---

## Provisioner

Executes scripts or commands after resource creation.

---

# Final Interview Tip

For DevOps interviews, always explain Terraform in this order:

```text
Provider
→ Resource
→ State
→ Variables
→ Modules
→ Provisioners
→ Backend
→ CI/CD Integration
```

This creates a strong professional explanation flow.
