Deploy  prometheus
```bash

kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-nodeport.yaml

```
Deploy  graphana
```bash

kubectl apply -f grafana-deployment.yaml
kubectl apply -f grafana-nodeport.yaml

```
🔹 Verify
```bash

kubectl get pods
kubectl get svc

```

Expected:

NAME	TYPE	PORT
prometheus-service	NodePort	30090
grafana-service	NodePort	30300
🔹 Add Prometheus in Grafana

In Grafana UI:

Configuration → Data Sources

Add Prometheus

URL:

http://prometheus-service:9090


Save & Test ✅






Access Grafana
http://<NODE-IP>:30300


Login:

User: admin

Password: admin