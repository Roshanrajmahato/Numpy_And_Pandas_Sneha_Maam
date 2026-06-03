https://chatgpt.com/share/699e47f7-8a6c-8012-bf58-29e51e3a9352

https://chatgpt.com/share/699e4791-753c-8012-9b66-8aa6b004dcb1

```bash
                     INTERNET
                         │
                         ▼
              Cloud Load Balancer
                         │
                         ▼
                 frontend-service
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      frontend-pod-1          frontend-pod-2
             │                    │
             │                    │
             ▼        Calls       ▼
                 backend-service
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
       backend-pod-1          backend-pod-2
```
