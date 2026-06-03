# 6. Write a Sample Dockerfile for Deploying Nginx

## Simple Interview Answer

A Dockerfile is a text file that contains instructions to build a Docker image automatically.

It defines:

* Base image
* Files to copy
* Commands to run
* Ports to expose
* Startup command

For deploying Nginx, we can create a Dockerfile that uses the official Nginx image and serves web content.

---

# What is Docker?

Docker is a containerization platform used to package applications and dependencies into lightweight containers.

Containers help applications run consistently across:

* Development
* Testing
* Production

---

# What is Nginx?

Nginx is a high-performance:

* Web server
* Reverse proxy
* Load balancer

It is commonly used to host websites and applications.

---

# Sample Dockerfile for Nginx

## Dockerfile

```dockerfile id="8a1c7x"
# Step 1: Use official nginx image
FROM nginx:latest

# Step 2: Copy website files into nginx html folder
COPY . /usr/share/nginx/html

# Step 3: Expose port 80
EXPOSE 80

# Step 4: Start nginx server
CMD ["nginx", "-g", "daemon off;"]
```

---

# Explanation of Each Line

---

## 1. FROM

```dockerfile id="m5f8yz"
FROM nginx:latest
```

### Purpose

* Defines the base image
* Downloads official Nginx image from Docker Hub

### Meaning

* `nginx` → image name
* `latest` → latest version tag

---

## 2. COPY

```dockerfile id="y9f1v2"
COPY . /usr/share/nginx/html
```

### Purpose

Copies website files from local system to container.

### Meaning

* `.` → current directory
* `/usr/share/nginx/html` → Nginx default web folder

---

## 3. EXPOSE

```dockerfile id="f3g2ka"
EXPOSE 80
```

### Purpose

Opens port 80 inside the container.

Nginx runs on port 80 by default.

---

## 4. CMD

```dockerfile id="a4q8tu"
CMD ["nginx", "-g", "daemon off;"]
```

### Purpose

Starts Nginx when container launches.

### Why `daemon off`?

Normally Nginx runs in background.
Docker containers need a foreground process to stay alive.

---

# Project Structure Example

```bash id="x5u2kj"
project/
│
├── Dockerfile
├── index.html
```

---

# Sample index.html

```html id="vx8b40"
<!DOCTYPE html>
<html>
<head>
    <title>My Nginx App</title>
</head>
<body>
    <h1>Welcome to Docker Nginx</h1>
</body>
</html>
```

---

# Steps to Build and Run Docker Container

---

## Step 1: Build Docker Image

```bash id="2hfylo"
docker build -t my-nginx-app .
```

### Explanation

* `docker build` → build image
* `-t` → tag name
* `.` → current directory

---

## Step 2: Run Container

```bash id="24zjlwm"
docker run -d -p 8080:80 my-nginx-app
```

### Explanation

* `-d` → detached mode
* `-p 8080:80`

  * 8080 → host machine port
  * 80 → container port

---

## Step 3: Access Application

Open browser:

```bash id="e50wnx"
http://localhost:8080
```

You will see:

```text
Welcome to Docker Nginx
```

---

# Dockerfile Workflow

```text
Dockerfile
   ↓
Docker Build
   ↓
Docker Image
   ↓
Docker Run
   ↓
Container Starts
```

---

# Important Dockerfile Instructions

| Instruction | Purpose                       |
| ----------- | ----------------------------- |
| `FROM`      | Base image                    |
| `COPY`      | Copy files                    |
| `RUN`       | Execute commands during build |
| `CMD`       | Default startup command       |
| `EXPOSE`    | Open port                     |
| `WORKDIR`   | Set working directory         |
| `ENV`       | Set environment variables     |

---

# Real-Time DevOps Example

Suppose a developer creates a frontend website.

Instead of installing:

* Nginx manually
* Dependencies manually
* Configurations manually

A Dockerfile automates everything.

Benefits:

* Same environment everywhere
* Fast deployment
* Easy scaling
* Portable application

---

# Multi-Stage Production Dockerfile (Advanced Interview Answer)

Sometimes interviewers ask for optimization.

Example:

```dockerfile id="7m9u1r"
FROM nginx:alpine

COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Why Alpine?

* Smaller image size
* Faster downloads
* Better for production

---

# Common Docker Commands

| Command         | Purpose          |
| --------------- | ---------------- |
| `docker build`  | Build image      |
| `docker run`    | Run container    |
| `docker ps`     | List containers  |
| `docker images` | List images      |
| `docker stop`   | Stop container   |
| `docker rm`     | Remove container |

---

# Common Interview Follow-Up Questions

## Why use Docker with Nginx?

Because Docker provides:

* Portability
* Isolation
* Easy deployment
* Faster scaling

---

## Difference Between Image and Container

| Image     | Container        |
| --------- | ---------------- |
| Blueprint | Running instance |
| Static    | Dynamic          |
| Read-only | Executable       |

---

# Short Interview Version (2-Minute Answer)

“A Dockerfile is a text file containing instructions to build a Docker image automatically. For deploying Nginx, we use the official Nginx base image, copy website files into the Nginx HTML directory, expose port 80, and start the Nginx server using the CMD instruction.

After creating the Dockerfile, we build the image using docker build and run the container using docker run. Docker helps package the application and Nginx server together for consistent deployment across environments.”
