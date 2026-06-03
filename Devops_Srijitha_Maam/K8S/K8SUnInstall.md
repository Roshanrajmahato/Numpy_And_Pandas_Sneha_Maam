
******************************************************
************* Uninstall Of Kubeernates ***************
******************************************************

🟡 STEP 1 – RESET KUBEADM (MOST IMPORTANT)
sudo kubeadm reset -f


✔ Removes:

cluster config

certificates

kubelet config

etcd data (on master)

🟡 STEP 2 – STOP SERVICES
sudo systemctl stop kubelet
sudo systemctl disable kubelet


Optional but good:

sudo systemctl stop containerd

🟡 STEP 3 – REMOVE PACKAGES
sudo apt purge -y kubeadm kubelet kubectl
sudo apt autoremove -y


✔ This removes binaries from:

/usr/bin/kubeadm

/usr/bin/kubectl

/usr/bin/kubelet

🟡 STEP 4 – DELETE DIRECTORIES
sudo rm -rf /etc/kubernetes
sudo rm -rf /var/lib/kubelet
sudo rm -rf /var/lib/etcd
sudo rm -rf /etc/cni
sudo rm -rf /opt/cni
sudo rm -rf /var/lib/cni


User kubeconfig:

rm -rf ~/.kube

🟡 STEP 5 – FLUSH IPTABLES (VERY IMPORTANT)
sudo iptables -F
sudo iptables -t nat -F
sudo iptables -t mangle -F
sudo iptables -X


Optional save:

sudo iptables-save | sudo tee /etc/iptables/rules.v4

🟡 STEP 6 – REMOVE CONTAINERD (FOR 100% FRESH)

👉 Only if you want completely new setup:

sudo apt purge -y containerd.io containerd
sudo rm -rf /etc/containerd
sudo rm -rf /var/lib/containerd

🟡 STEP 7 – REMOVE K8s REPO
sudo rm -f /etc/apt/sources.list.d/kubernetes.list
sudo rm -f /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo apt update


✔ Your path was slightly wrong — key is in:
/etc/apt/keyrings/ (not /usr/share)

🟡 STEP 8 – REBOOT (REQUIRED)
sudo reboot

✅ AFTER REBOOT — VERIFY CLEAN STATE
which kubeadm
which kubectl
which kubelet


👉 Should return nothing

kubeadm version
kubectl version --client


👉 Should say: command not found

 