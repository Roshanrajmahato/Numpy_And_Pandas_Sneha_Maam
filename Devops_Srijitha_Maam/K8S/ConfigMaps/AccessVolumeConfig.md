You are currently in:

```bash id="f9d3xn"
root@work2:~#
```

That is the root user's home directory.

The ConfigMap mounted files are NOT stored there.

They are stored under kubelet directory.

---

# Go to Kubernetes Pod Storage

Run:

```bash id="yc8qvf"
cd /var/lib/kubelet/pods/
```

Now check all pod folders:

```bash id="xtg5fx"
ls
```

You will see many long UID directories like:

```bash id="y9v7h8"
8d9c9f77-6b7e-4b5e-a4b1-123456789abc
```

---

# Find Correct Pod UID

From master node run:

```bash id="ktvdd9"
kubectl get pod configmap-volpod -n configmaps -o yaml | grep uid
```

Example:

```bash id="0m8rlm"
uid: 8d9c9f77-6b7e-4b5e-a4b1-123456789abc
```

Copy this UID.

---

# Open That Pod Folder on Worker Node

Example:

```bash id="ybk15u"
cd /var/lib/kubelet/pods/8d9c9f77-6b7e-4b5e-a4b1-123456789abc
```

Now check:

```bash id="4qlf1q"
ls
```

You will see folders like:

```bash id="kx8jef"
containers
plugins
volumes
etc-hosts
```

---

# Open Volumes Directory

Run:

```bash id="4g9t2n"
cd volumes
ls
```

Output:

```bash id="4bs8g6"
kubernetes.io~configmap
kubernetes.io~projected
```

---

# Open ConfigMap Volume

Run:

```bash id="qg1p4f"
cd kubernetes.io~configmap
ls
```

Example:

```bash id="2j9qjt"
config-volume
```

Go inside:

```bash id="nfrzy2"
cd config-volume
ls
```

Now you will finally see:

```bash id="08y7x7"
DB_HOST
DB_PORT
DB_NAME
```

---

# Read File Content

Example:

```bash id="t2bhc4"
cat DB_HOST
```

---

# Why You Couldn't Find `/config`

Because:

```text id="s2zwzb"
/config
```

exists INSIDE the container only.

It does NOT exist directly on Worker Node root filesystem.

Kubernetes maps:

```text id="mln7m7"
Worker Node Path
↓
/var/lib/kubelet/pods/<uid>/volumes/kubernetes.io~configmap/config-volume/
```

into container path:

```text id="06m6kl"
/config
```

using Linux mount namespaces.
