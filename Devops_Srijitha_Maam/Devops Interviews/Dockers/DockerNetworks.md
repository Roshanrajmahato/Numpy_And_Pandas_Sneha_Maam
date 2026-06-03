# 7. Types of Docker Network. Which is the Default Network?

## Simple Interview Answer

Docker networking allows containers to communicate with:

* Other containers
* Host machine
* External internet

Docker provides different network types based on application requirements.

The main Docker network types are:

1. Bridge Network
2. Host Network
3. None Network
4. Overlay Network
5. Macvlan Network

The default Docker network is:

# **Bridge Network**

---

# Why Docker Networking is Needed?

Containers are isolated by default.

Networking helps containers:

* Communicate with each other
* Access external services
* Expose applications to users

Example:

* Frontend container communicates with backend container
* Backend connects to database container

---

# Types of Docker Networks

---

# 1. Bridge Network (Default Network)

## What is it?

Bridge network is the default network created by Docker.

When a container is started without specifying a network, Docker automatically connects it to the bridge network.

---

## How it Works

Docker creates a virtual bridge:

```text id="ov9ysj"
docker0
```

Containers connected to this bridge can communicate with each other using:

* IP addresses
* Container names

---

## Example

Run container:

```bash id="m76duj"
docker run -d nginx
```

This container automatically joins the bridge network.

---

## Check Networks

```bash id="7ejg0h"
docker network ls
```

Example Output:

```text id="3xtclx"
NETWORK ID     NAME      DRIVER
xxxx           bridge    bridge
xxxx           host      host
xxxx           none      null
```

---

## Advantages

* Easy to use
* Default configuration
* Good for standalone containers

---

## Use Case

* Small applications
* Single-host communication

---

# 2. Host Network

## What is it?

In host networking, the container shares the host machine’s network directly.

No separate container IP is created.

---

## Example

```bash id="tbw56s"
docker run --network host nginx
```

---

## Characteristics

* Faster performance
* No network isolation
* Uses host ports directly

---

## Advantages

* Better speed
* Lower latency

---

## Disadvantages

* Less security
* Port conflicts possible

---

## Use Case

High-performance applications.

---

# 3. None Network

## What is it?

The container gets completely isolated from networking.

No:

* Internet
* External communication
* Container communication

---

## Example

```bash id="t13n9m"
docker run --network none nginx
```

---

## Use Case

* Security testing
* Fully isolated applications

---

# 4. Overlay Network

## What is it?

Overlay network allows containers running on multiple Docker hosts to communicate.

Mainly used in:

* Docker Swarm
* Distributed environments

---

## Characteristics

* Multi-host networking
* Secure communication

---

## Use Case

Microservices running across multiple servers.

---

# 5. Macvlan Network

## What is it?

Macvlan assigns a MAC address to each container.

Containers appear like physical devices on the network.

---

## Advantages

* Direct network access
* Better network visibility

---

## Use Case

Applications needing direct LAN access.

---

# Docker Network Drivers Summary

| Network Type | Description                    |
| ------------ | ------------------------------ |
| Bridge       | Default private network        |
| Host         | Shares host network            |
| None         | No networking                  |
| Overlay      | Multi-host communication       |
| Macvlan      | Direct physical network access |

---

# Which is the Default Docker Network?

## Answer:

# Bridge Network

Docker automatically creates:

```text id="i6qjj7"
bridge
```

Whenever a container starts without specifying a network, it joins the bridge network automatically.

---

# How to Create Custom Bridge Network

```bash id="9hdfrg"
docker network create mynetwork
```

Run container using custom network:

```bash id="4gxvll"
docker run -d --network mynetwork nginx
```

---

# How Containers Communicate

Suppose:

* App container
* Database container

Both connected to same network.

They can communicate using container names.

Example:

```text id="t6u4zt"
app-container → db-container
```

This is commonly used in microservices.

---

# Real-Time Example

Suppose an application has:

* Frontend container
* Backend container
* Database container

Using Docker networking:

* Frontend talks to backend
* Backend talks to database

All communication happens securely inside Docker network.

---

# Important Docker Network Commands

| Command                  | Purpose                      |
| ------------------------ | ---------------------------- |
| `docker network ls`      | List networks                |
| `docker network create`  | Create network               |
| `docker network inspect` | View network details         |
| `docker network rm`      | Remove network               |
| `docker network connect` | Connect container to network |

---

# Interview Follow-Up Questions

## Difference Between Bridge and Host Network

| Bridge                     | Host                |
| -------------------------- | ------------------- |
| Isolated container network | Shares host network |
| Separate container IP      | Uses host IP        |
| More secure                | Less secure         |
| Slightly slower            | Faster              |

---

## Why Use Custom Bridge Network?

Benefits:

* Better isolation
* DNS-based container communication
* Easier management

---

# Docker Networking Architecture

```text id="12vwpr"
Container A
      │
      ▼
Bridge Network
      │
      ▼
Container B
```

---

# Short Interview Version (2-Minute Answer)

“Docker networking allows containers to communicate with each other and external systems. The main Docker network types are Bridge, Host, None, Overlay, and Macvlan.

The default Docker network is the Bridge network. When a container starts without specifying a network, Docker automatically connects it to the bridge network.

Bridge is commonly used for container-to-container communication on a single host, while Overlay is used for multi-host communication in Docker Swarm environments.”
