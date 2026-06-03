Create:-
backend-deployment.yaml ` nano backend-deployment.yaml        `
backend-clusterip.yaml ` nano backend-clusterip.yaml  `
frontend-deployment.yaml  ` nano frontend-deployment.yaml  `
frontend-nodeport.yaml ` frontend-nodeport.yaml  `

2. Deploy Backend
```bash

kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-clusterip.yaml

```

2. Deploy Frontend
```bash

kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-nodeport.yaml

```


Check:

```bash

kubectl get pods
kubectl get svc

```

TEST INTERNAL COMMUNICATION
Login into frontend pod
>runcmd
        > `  kubectl exec -it <frontend-pod-name> -- sh  `

Call backend using SERVICE NAME
>runcmd
        > ` curl http://backend-service  `

Output:
Hello from Backend
✅ This proves:-
Frontend → Backend communication using ClusterIP works.