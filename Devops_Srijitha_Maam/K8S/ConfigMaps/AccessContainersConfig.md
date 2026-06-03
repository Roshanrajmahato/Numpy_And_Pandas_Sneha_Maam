Your Pod `configmap-volpod` is running on worker node `work2`.

You are asking how to access the actual container from the Worker Node itself.

---

# Step 1 — SSH Into Worker Node

You already did:

```bash id="f6c9uh"
ssh ubuntu@work2
```

Then:

```bash id="ghl9wx"
sudo -i
```

Good.

---

# Step 2 — Check Container Runtime

Run:

```bash id="7h1mlv"
crictl ps
```

OR:

```bash id="y2m5w8"
docker ps
```

depending on runtime.

In kubeadm clusters, usually:

* containerd → use `crictl`
* Docker → use `docker`

Most likely you use `containerd`.

---

# Step 3 — Find Your Pod Container

Run:

```bash id="3yjlwm"
crictl ps
```

Example output:

```bash id="zw2wzr"
CONTAINER           IMAGE         CREATED         STATE     NAME              POD
a1b2c3d4e5f6       nginx         10 mins ago    Running   config-container  configmap-volpod
```

Find:

```bash id="52n40n"
configmap-volpod
```

Copy container ID.

Example:

```bash id="9r9l3h"
a1b2c3d4e5f6
```

---

# Step 4 — Enter Container

Run:

```bash id="8i8gkp"
crictl exec -it a1b2c3d4e5f6 sh
```

Now you are INSIDE the container.

Prompt changes like:

```bash id="7fjlwm"
/ #
```

---

# Step 5 — Access `/config`

Run:

```bash id="0l4b49"
cd /config
ls
```

Output:

```bash id="1r9g6u"
DB_HOST
DB_PORT
DB_NAME
```

Read file:

```bash id="jlwm7z"
cat DB_HOST
```

---

# Full Real Flow

## On Worker Node

```bash id="b0h9ww"
sudo -i
crictl ps
```

Copy container ID.

Then:

```bash id="mjjlwm"
crictl exec -it <container-id> sh
```

Then inside container:

```bash id="4o8zpu"
cd /config
ls
cat DB_HOST
```

---

# Architecture Understanding

```text id="qjlwmr"
Worker Node (work2)
    ↓
containerd runtime
    ↓
Container created
    ↓
ConfigMap mounted into container
    ↓
Accessible at /config
```

---

# If `crictl` Command Not Found

Install/configure it:

```bash id="1rjlwm"
sudo crictl ps
```

If needed:

```bash id="5k0b0v"
sudo crictl config runtime-endpoint unix:///run/containerd/containerd.sock
```

---

# Alternative Using containerd Directly

You can also use:

```bash id="jlwmw0"
ctr -n k8s.io containers ls
```

But `crictl` is easier and recommended for Kubernetes debugging.
