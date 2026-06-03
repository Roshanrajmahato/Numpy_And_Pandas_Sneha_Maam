# On MASTER EC2 ##

1️⃣ Create master.sh
>runcmd
        >`   nano master.sh     `
        >`   vim master.sh     `

Save file:
👉 Press  Ctrl + X → Y → Enter
👉 Press  Ctrl + O → Enter Then Ctrl + X

2️⃣ Make it executable
>runcmd
        > `  chmod +x master.sh   `

3️⃣ RUN MASTER SCRIPT
>runcmd 
        >  `  sudo ./master.sh   `

```bash

#!/bin/bash
set -e

echo "===================================================="
echo "      KUBERNETES MASTER NODE SETUP"
echo "===================================================="

# ---------- ROOT CHECK ----------
if [[ $EUID -ne 0 ]]; then
   echo "❌ Run as root: sudo ./master.sh"
   exit 1
fi

echo "=== OS Preparation ==="
apt update -y
apt upgrade -y

# ---------- TIME SYNC (VERY IMPORTANT) ----------
apt install -y chrony
systemctl enable chrony
systemctl restart chrony

# ---------- DISABLE SWAP ----------
swapoff -a
sed -i '/ swap / s/^/#/' /etc/fstab

# ---------- KERNEL MODULES ----------
echo "=== Kernel Modules ==="
cat <<EOF > /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

modprobe overlay
modprobe br_netfilter

# ---------- SYSCTL ----------
cat <<EOF > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
EOF

sysctl --system

# ---------- INSTALL CONTAINERD ----------
echo "=== Install containerd ==="
apt install -y ca-certificates curl apt-transport-https
mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
tee /etc/apt/keyrings/docker.asc > /dev/null

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
> /etc/apt/sources.list.d/docker.list

apt update -y
apt install -y containerd.io

systemctl enable containerd
systemctl start containerd

# ---------- CONFIGURE CONTAINERD ----------
echo "=== Configure containerd ==="
mkdir -p /etc/containerd

containerd config default > /etc/containerd/config.toml

# >>> MAIN FIX <<<
sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

systemctl restart containerd

# ---------- FIREWALL RULE ----------
iptables -P FORWARD ACCEPT || true

# ---------- INSTALL KUBERNETES ----------
echo "=== Install Kubernetes ==="

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | \
gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] \
https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" \
> /etc/apt/sources.list.d/kubernetes.list

apt update -y
apt install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl

# ---------- PULL IMAGES ----------
echo "=== Pulling Images ==="
kubeadm config images pull

# ---------- INIT CLUSTER ----------
echo "=== Initialize Master ==="

kubeadm init --pod-network-cidr=10.244.0.0/16

# ---------- KUBECTL CONFIG ----------
echo "=== Setup Kubectl ==="
mkdir -p $HOME/.kube
cp /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

# ---------- INSTALL CNI ----------
echo "=== Install Flannel CNI ==="
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

# ---------- VALIDATION ----------
echo "======================================="
echo " VALIDATION"
echo "======================================="

echo "[1] Containerd:"
systemctl is-active containerd

echo "[2] Kubelet:"
systemctl is-active kubelet || true

echo "[3] Nodes:"
kubectl get nodes || true

echo "======================================="
echo "🚀 MASTER NODE READY"
echo "======================================="

echo ""
echo "👉 WORKER NODE JOIN COMMAND USED WITH SUDO:"
kubeadm token create --print-join-command
echo ""


```

Save file:
👉 Press  Ctrl + X → Y → Enter
👉 Press  Ctrl + O → Enter Then Ctrl + X

2️⃣ Make it executable
>runcmd
        > `  chmod +x master.sh   `

3️⃣ RUN MASTER SCRIPT
>runcmd 
        >  `  sudo ./master.sh   `

#️⃣#️⃣👉👉DO IT FIRST THEN JOIN WORKER NODE 👈👈#️⃣#️⃣#️⃣#️⃣

#️⃣#️⃣#️⃣#️⃣👉👉RUN THIS ON MASTER NODE ! BEFORE JOINING TO WORKER NODE>👈👈#️⃣#️⃣#️⃣#️⃣

🚩🚩 IF ERROR nOt because of script so execute it 🚩🚩
error:~
al tcp 127.0.0.1:8080: connect: connection refused
The connection to the server localhost:8080 was refused - did you specify the right host or port?
Then 
👉👉Then Just RUN :~👈👈
```bash

mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

```

👉 NOW INSTALLED CNI In MASTER ONLY

After kubeadm init, you MUST install network plugin.

Run on control-plane:

>runcmd
        > `  kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/calico.yaml   `



Check The Status of Node its Ready or Not
>runcmd
       >` kubectl get nodes  `


#️⃣🤜👉 NOW JOIN THE WORKER NODE THE JOIN COMMAND OUTPUT OF MASTER 👈🤛#️⃣

kubeadm join 172.x.x.x:6443 --token xxxx --discovery-token-ca-cert-hash sha256:xxxx

sudo kubeadm join 172.31.19.160:6443 --token je8hqa.sptnwib0s3yhd367 --discovery-token-ca-cert-hash sha256:498d94177a6ea0974edaeeda99624f8ddeb176fbedd7e9e4bbdbd37430cd28bb

#️⃣1️⃣
👉Check kubelet on each node if its NotReady
👉Run on ALL nodes its NotReady
👉(ctl, node1, node2, node3)

```bash
sudo systemctl restart kubelet
sudo systemctl enable kubelet
```


#️⃣2️⃣
👉 Nodes will become → Ready
👉 Check Container Runtime On Nodes:-
```bash

sudo crictl ps
sudo systemctl status containerd



#  #️⃣ Now On WORKER EC2 #️⃣

1️⃣ Create worker.sh
>runcmd
        >`  nano worker.sh  `
        >`  vim worker.sh  `


```bash

#!/bin/bash
set -e

echo "====================================================="
echo " Kubernetes Worker Node - Enterprise Grade Setup"
echo "====================================================="

# ---------- ROOT CHECK ----------
if [[ $EUID -ne 0 ]]; then
   echo "❌ Run as root: sudo ./worker.sh"
   exit 1
fi

# ---------- BASIC TOOLS ----------
apt-get update
apt-get install -y curl wget apt-transport-https ca-certificates gnupg lsb-release chrony

# ---------- TIME SYNC (CRITICAL) ----------
systemctl enable chrony
systemctl restart chrony

# ---------- DISABLE SWAP ----------
swapoff -a
sed -i '/ swap / s/^/#/' /etc/fstab

# ---------- KERNEL MODULES ----------
cat <<EOF > /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

modprobe overlay
modprobe br_netfilter

# ---------- SYSCTL ----------
cat <<EOF > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

sysctl --system

# ---------- INSTALL CONTAINERD ----------
apt-get update
apt-get install -y containerd

# ---------- CONTAINERD CONFIG ----------
systemctl stop containerd || true
mkdir -p /etc/containerd

containerd config default > /etc/containerd/config.toml

# >>> MAIN FIX <<<
sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

systemctl daemon-reload
systemctl enable containerd
systemctl restart containerd

# ---------- INSTALL CNI PLUGINS ----------
echo "Installing CNI Plugins..."

CNI_VERSION="v1.4.0"
wget -q https://github.com/containernetworking/plugins/releases/download/${CNI_VERSION}/cni-plugins-linux-amd64-${CNI_VERSION}.tgz

mkdir -p /opt/cni/bin
tar -C /opt/cni/bin -xzvf cni-plugins-linux-amd64-${CNI_VERSION}.tgz

# ---------- INSTALL CRICTL ----------
VERSION="v1.30.0"
wget -q https://github.com/kubernetes-sigs/cri-tools/releases/download/${VERSION}/crictl-${VERSION}-linux-amd64.tar.gz
tar -C /usr/local/bin -xzvf crictl-${VERSION}-linux-amd64.tar.gz

cat <<EOF > /etc/crictl.yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
debug: false
EOF

# ---------- KUBERNETES REPO ----------
mkdir -p /etc/apt/keyrings

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | \
gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] \
https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" > /etc/apt/sources.list.d/kubernetes.list

apt-get update

# ---------- INSTALL K8S ----------
apt-get install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl

systemctl enable kubelet
systemctl restart kubelet

# ---------- FIREWALL SAFE RULES ----------
iptables -P FORWARD ACCEPT || true

# ---------- VERIFICATION ----------
echo "========================================"
echo " VALIDATION CHECKS"
echo "========================================"

echo "[1] Containerd Status:"
systemctl is-active containerd

echo "[2] CRI Status:"
crictl info | grep RuntimeReady || true

echo "[3] Kubelet Status:"
systemctl is-active kubelet || true

echo ""
echo "========================================"
echo "👉 NOW RUN COMMAND FOR JOIN WORKER NODE FROM MASTER WITH SUDO:"
echo "sudo kubeadm join <MASTER-IP>:6443 --token <TOKEN> --discovery-token-ca-cert-hash sha256:<HASH>"
echo "========================================"

```

Save file:
👉 Press  Ctrl + X → Y → Enter
👉 Press  Ctrl + O → Enter Then Ctrl + X

2️⃣ Execute worker.sh
>runcmd
        > `  chmod +x worker.sh   `

3️⃣ RUN worker SCRIPT
>runcmd 
        >  `  sudo ./worker.sh   `

#️⃣ Only In Worker Node #️⃣
4️⃣ Join the worker node with Join Command

🤜👉 Paste THE JOIN COMMAND Only in Worker node 👈🤛

kubeadm join 172.x.x.x:6443 --token xxxx --discovery-token-ca-cert-hash sha256:xxxx
or
sudo kubeadm join 172.x.x.x:6443 --token ... --discovery-token-ca-cert-hash sha256:...

Example:~

kubeadm join 172.31.37.82:6443 --token to16b3.gk8bbbsuwtdyudjn \
        --discovery-token-ca-cert-hash sha256:897241df51441e397b977627d4d1eabf072e59b0d6d7ed783eba4b448947b9f9

or 
sudo kubeadm join 172.31.18.134:6443 --token 5h3k20.jadddsdkhw2wmcsw --discovery-token-ca-cert-hash sha256:265c0aaec8b601310cc54a17bbfaa8be1f251cf46b30231c0e849272eae4a6ea

kubeadm join 172.31.35.202:6443 --token 4lth11.e4s2ax9t6h8xcrt4 --discovery-token-ca-cert-hash sha256:c3f7f9a55181aac2e63595a755f482fa0dab6bd442975c4923c0eb8ac0fcf7b3

5️⃣ VERIFY (On MASTER)

>runcmd
        > `  kubectl get nodes  `

>runcmd 
        > ` kubectl get pods -A `


sudo kubeadm join 172.31.45.110:6443 --token 1akwqz.522ievsfcqit0jz7 \
        --discovery-token-ca-cert-hash sha256:b34fe2fe7979177804397d095f6687059f63319b414fa70e8f5b4aea58e01b51
 