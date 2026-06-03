If using Docker:
>runcmd
       > ` sodu hostname NameYouWant  ` Then Refreash

sodu hostname nameYouWant

1️⃣ See which app (Pod) is running on node2
>runcmd
       > ` sudo crictl ps  `

If using Docker:
>runcmd
       > ` docker ps  `

👉 Command For Persistent Volume  (PV) 👈

>runcmd
       > ` kubectl create -f pv.yml  `

>runcmd
       > ` kubectl get pv  `

>runcmd
       > ` kubectl describe pv pv_name  `
       > ` kubectl describe pv example-pv `

👉 Command For Persistent Volume Claim (PVC) 👈

>runcmd
       > ` kubectl create -f pvc.yml  `

>runcmd
       > ` kubectl get pvc  `

>runcmd
       > ` kubectl describe pvc pvc_name  `
       > ` kubectl describe pvc ebs-pvc  `


👉 Pods Service 👈
To Get The pods Service
>runcmd
       > ` kubectl get pods  `
       > ` kubectl get pods -o wide `

To Delete pods Services
>runcmd
       > ` kubectl delete pods pods_name  `
       > ` kubectl delete pods example-pv-pods  `
      

👉 PV Service 👈
To Get The PV Service
>runcmd
       > ` kubectl get pv  `

To Delete PV Services
>runcmd
       > ` kubectl delete pv pv_name  `
       > ` kubectl delete pv example-pv  `


👉 PVC Service 👈
To Get The PVC Service
>runcmd
       > ` kubectl get pvc  `

To Delete PVC Services
>runcmd
       > ` kubectl delete pvc pvc_name  `
       > ` kubectl delete pvc ebs-pvc  `


👉 To get the namespace  👈

👉 To get the namespace pod 👈

>runcmd
       > ` kubectl get pods -n namespace_name -o wide  `
       > ` kubectl get pods -n dev-team -o wide  `


# To delete the pods

✅ 1. Delete ALL pods in the current namespace
kubectl delete pods --all


👉 Deletes every pod in the namespace you are currently using.

✅ 2. Delete pods from a specific namespace
kubectl delete pods --all -n <namespace>


Example:

kubectl delete pods --all -n default

✅ 3. Delete pods across ALL namespaces
kubectl delete pods --all --all-namespaces


⚠️ Be careful:
This removes pods from system namespaces like:

kube-system

kube-public

kube-node-lease

⚠️ Important Reality (Interview Concept)
If pods are created by:

Deployment

ReplicaSet

DaemonSet

StatefulSet

Job

👉 They will be recreated immediately after deletion!

Because controllers maintain desired state.

💡 If you REALLY want to stop them permanently
▶ Delete Deployment (recommended)
kubectl delete deployment --all
This removes:-deployments

▶ Delete everything in namespace
kubectl delete all --all
This removes:-pods,services,deployments,replicasets,statefulsets,daemonsets

🔎 Check before deleting
See all pods first
kubectl get pods -A

Dry run (safe check)
kubectl delete pods --all --dry-run=client



kubectl logs <pod-name or id > -n three-tier -f

kubectl logs frontend-58d9bc4cdc-rrqkw -n three-tier -c <container-name> -f

kubectl describe pod api-6cd659b8d4-mhnpf -n three-tier
