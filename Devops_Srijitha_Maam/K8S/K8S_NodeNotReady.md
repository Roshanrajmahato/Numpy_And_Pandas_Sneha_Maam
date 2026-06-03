Check The Status of Node its NotReady
>runcmd
       >` kubectl get nodes  `

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


```






1️⃣ Check kubelet on each node

Run on ALL nodes (ctl, node1, node2, node3):

>runcmd
       > ` sudo systemctl status kubelet  `

Not running:

```bash
sudo systemctl restart kubelet
sudo systemctl enable kubelet
```

2️⃣ MOST COMMON → CNI NOT INSTALLED

After kubeadm init, you MUST install network plugin.

Install Calico (recommended)

Run on control-plane:

kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/calico.yaml


Then wait:

watch kubectl get nodes


👉 Nodes will become → Ready

3️⃣ Check container runtime

On nodes:

sudo crictl ps
sudo systemctl status containerd


>runcmd
       > ` sudo systemctl status kubelet  `


>runcmd
       > ` sudo systemctl restart kubelet  `
       > ` sudo systemctl enable kubelet  `

```bash

sudo apt update && sudo apt upgrade -y
sudo swapoff -a
sudo sed -i '/ swap / s/^/#/' /etc/fstab

```


🎯 Most Common Reason (Very Important)

If you have ONLY ONE MASTER NODE, it has a taint like:

`node-role.kubernetes.io/control-plane:NoSchedule`


That prevents pods from running.

Fix:

kubectl taint nodes --all node-role.kubernetes.io/control-plane-


Then pods will start immediately.