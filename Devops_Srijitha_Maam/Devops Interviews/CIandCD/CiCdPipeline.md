# 10. Write a Sample CI/CD Pipeline and Explain the Steps

## Simple Interview Answer

A CI/CD pipeline is an automated workflow that:

* Builds application code
* Runs tests
* Creates deployment packages
* Deploys applications automatically

The pipeline helps deliver software faster and more reliably with minimal manual work.

A typical CI/CD pipeline includes:

1. Source Stage
2. Build Stage
3. Test Stage
4. Deploy Stage

---

# What is a Pipeline?

A pipeline is a sequence of automated steps executed whenever developers push code to a repository.

Example Flow:

```text id="c4xl1m"
Developer Pushes Code
        ↓
Build Application
        ↓
Run Tests
        ↓
Create Docker Image
        ↓
Deploy Application
```

---

# Sample Jenkins CI/CD Pipeline

## Jenkinsfile

```groovy id="nhjk46"
pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/example/project.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Application'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker Image'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application'
            }
        }
    }
}
```

---

# Explanation of Pipeline Steps

---

# 1. Agent

```groovy id="68x2cg"
agent any
```

### Purpose

Defines where the pipeline runs.

### Meaning

* `any` means Jenkins can run the pipeline on any available agent/node.

---

# 2. Stages

```groovy id="nuz8z4"
stages {
}
```

### Purpose

Contains all pipeline phases.

Each stage performs one specific task.

---

# 3. Clone Code Stage

```groovy id="5qt1lw"
stage('Clone Code')
```

### Purpose

Downloads source code from Git repository.

### Example

```groovy id="i2rkdd"
git 'https://github.com/example/project.git'
```

### Why Needed?

Pipeline needs latest application code.

---

# 4. Build Stage

```groovy id="7dkbhf"
stage('Build')
```

### Purpose

Compiles application and installs dependencies.

Examples:

* Java → Maven build
* Node.js → npm install
* Python → pip install

---

## Example Build Commands

### Java

```bash id="66lxvz"
mvn clean package
```

### Node.js

```bash id="7y24k8"
npm install
```

---

# 5. Test Stage

```groovy id="dfm7t4"
stage('Test')
```

### Purpose

Runs automated tests.

### Types of Tests

* Unit Testing
* Integration Testing
* API Testing

### Benefits

* Detect bugs early
* Improve code quality

---

# 6. Docker Build Stage

```groovy id="9iym6x"
stage('Docker Build')
```

### Purpose

Creates Docker image for application.

Example:

```bash id="z2hlnv"
docker build -t myapp .
```

### Why?

Application becomes portable and deployable anywhere.

---

# 7. Deploy Stage

```groovy id="6r5n51"
stage('Deploy')
```

### Purpose

Deploys application to:

* Server
* Cloud
* Kubernetes cluster

Example:

```bash id="7qywx6"
kubectl apply -f deployment.yaml
```

---

# CI/CD Pipeline Workflow in Real Time

Suppose a developer updates an application.

---

## Step-by-Step Flow

### Step 1: Developer Pushes Code

Developer pushes code to:

* GitHub
* [GitHub](https://github.com?utm_source=chatgpt.com)

---

### Step 2: Jenkins Triggered

Jenkins automatically detects code changes.

---

### Step 3: Build Starts

Application gets compiled.

---

### Step 4: Automated Tests Run

Testing verifies application quality.

If tests fail:

* Pipeline stops automatically.

---

### Step 5: Docker Image Created

Docker image is generated.

---

### Step 6: Deployment Happens

Application deploys to:

* Server
* Cloud
* Kubernetes cluster

---

# CI/CD Pipeline Architecture

```text id="lx9w9f"
Developer
   ↓
Git Repository
   ↓
Jenkins Pipeline
   ↓
Build
   ↓
Test
   ↓
Docker Image
   ↓
Deployment
   ↓
Production
```

---

# Benefits of CI/CD Pipeline

| Benefit              | Explanation                |
| -------------------- | -------------------------- |
| Faster Delivery      | Quick software releases    |
| Automation           | Less manual work           |
| Better Quality       | Automated testing          |
| Reliable Deployments | Consistent release process |
| Faster Bug Detection | Errors identified early    |
| Scalability          | Easy deployment management |

---

# Common CI/CD Pipeline Tools

| Tool           | Purpose                  |
| -------------- | ------------------------ |
| Jenkins        | Automation               |
| GitHub Actions | GitHub CI/CD             |
| GitLab CI/CD   | Integrated DevOps        |
| Docker         | Containerization         |
| Kubernetes     | Deployment orchestration |

---

# Advanced CI/CD Stages (Interview Advantage)

Modern pipelines may include:

* Security scanning
* Code quality analysis
* Performance testing
* Infrastructure provisioning

### Popular Tools

* SonarQube
* Terraform

---

# Important Interview Follow-Up Questions

---

## What Happens if Build Fails?

Pipeline stops immediately.

Developer fixes issue and pushes code again.

---

## Why is Automation Important?

Automation:

* Saves time
* Reduces human errors
* Improves consistency

---

## What is Pipeline as Code?

Pipeline configuration stored in code format.

Benefits:

* Version control
* Reusability
* Easy collaboration

---

# Short Interview Version (2-Minute Answer)

“A CI/CD pipeline is an automated workflow used to build, test, and deploy applications. It helps deliver software faster and more reliably.

A typical pipeline includes stages like source code checkout, build, testing, Docker image creation, and deployment. Tools like GitHub, Jenkins, Docker, and Kubernetes are commonly used.

Whenever developers push code, the pipeline automatically runs all stages, detects errors early, and deploys applications with minimal manual effort.”
