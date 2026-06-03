https://chatgpt.com/c/697ea272-41ac-8323-9168-acb4b2176c45

1️⃣ Create EBS Volume in AWS
Go to AWS Console → EC2 → Volumes → Create Volume
Example:
Size: 5 GiB
Type: gp2 / gp3
Availability Zone: ⚠ MUST be same as worker node
After creation Volume:👉 volume-id = vol-0abcd1234


2️⃣First Check Your Kubernetes Version
>Runcmd 
       > ```  kubectl version ``` 

Use Compatible Version Only
Example:
If your cluster = 1.26
You must use aws-ebs-csi-driver driver compatible with 1.26
Your cluster is:
👉 Kubernetes 1.30.14 (Client + Server both)
✅ aws-ebs-csi-driver → release-1.30

3️⃣ Install CORRECT CSI Driver for K8s 1.30
✅ Use this exact command:
>runcmd 
       > ```    kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.30"         ```

4️⃣ Verify Installation
>runcmd
       > ```   kubectl get pods -n kube-system | grep ebs   ```
You must see:~
ebs-csi-controller (1 replica)
ebs-csi-node (on each node)

5️⃣ Check csidriver
>runcmd
        > ```   kubectl get csidriver     ```

Output should contain:`
ebs.csi.aws.com


#️⃣#️⃣ Creating A YAML File #️⃣#️⃣
*** Creating A These File ***
Create This File only No Need of ebspv.yaml(pv files) as it is automatically dynamically going created
storageclass.yaml
ebspvc.yaml
ebspod.yaml

1️⃣ Run StorageClass.yaml,ebspvc.yaml,ebspod.yaml

```bash

kubectl apply -f storageclass.yaml
kubectl apply -f ebspvc.yaml
kubectl apply -f ebspod.yaml

```


# Uninstall
✅ STEP-BY-STEP FIX FOR YOUR EXACT VERSION
Clean Wrong Installation First
Run this:

kubectl delete deployment ebs-csi-controller -n kube-system
kubectl delete daemonset ebs-csi-node -n kube-system
kubectl delete csidriver ebs.csi.aws.com


Ignore “not found” errors.

