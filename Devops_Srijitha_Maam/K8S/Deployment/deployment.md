https://chatgpt.com/share/69847efc-298c-8012-96b2-7bb1061c09c1

#️⃣#️⃣ Creating A YAML File #️⃣#️⃣
*** Creating A These File ***
👉Create This File only No Need of ebspv.yaml(pv files) as it is automatically dynamically going created
deployment.yaml  `  nano deployment.yaml  `

>runcmd
       > ` kubectl create -f deployment.yaml  ` Or Bootom One

>runcmd
       > ` kubectl get deployments  `
       > ` kubectl get pods  `
       > ` kubectl get rs  `


| Feature               | Main Command                  |
| ----------------------|-------------------------------|
| 1️⃣ Replica Management| `kubectl scale`               |
| 2️⃣Declarative Update | `kubectl apply` / `set image` |
| 3️⃣Rolling Update     | `kubectl rollout status`      |
| 4️⃣Rollback           | `kubectl rollout undo`        |
| 5️⃣Version History    | `kubectl rollout history`     |

1️⃣ Replica Management
👉Scale replicas manually
>runcmd
        > `  kubectl scale deployment nginx-deployment --replicas=5  `

Try To Crashes Pod 
>runcmd
        >  `  kubectl delete pod <pod-name> `
👉 Kubernetes will immediately create a new Pod , Because Deployment guarantees desired state.
b Declarative Updates(Particular Version)
👉 I want 3 replicas of nginx version 1.25
>runcmd
        > `  kubectl set image deployment/nginx-deployment nginx-container=nginx:1.25  `

👉To apply updates on deployment.ymal 
>rumcmd
        > `  kubectl apply -f deployment.yaml   `

3️⃣ Rolling Updates
👉Change image version
>runcmd
       >`  kubectl set image deployment/nginx-deployment nginx-container=nginx:1.26   `

👉Watch progress
>runcmd
        >` kubectl rollout status deployment nginx-deployment  `

4️⃣ Rollbacks
👉 Go back to previous stable version
>rumcmd
        > ` kubectl rollout undo deployment nginx-deployment  `

👉 Application recovers instantly

5️⃣ Version Control (History)
👉Check history
>runcmd
        > ` kubectl rollout history deployment nginx-deployment  `

👉See specific revision
>runcmd
        > ` kubectl rollout history deployment nginx-deployment --revision=2  `