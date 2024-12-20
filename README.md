# My Application Deployment

This repository contains Kubernetes manifests for deploying a sample application using ArgoCD.

## Files
- `deployment.yaml`: Defines the deployment for the application.
- `service.yaml`: Sets up a load-balanced service for the application.
- `configmap.yaml`: Contains configuration values.
- `secret.yaml`: Holds sensitive information like passwords.

## Deploying with ArgoCD
1. Set up an ArgoCD `Application` resource pointing to this repository and the `/application` directory.
2. ArgoCD will automatically sync the manifests and manage your application in the specified Kubernetes cluster.



## commands

 - Get argocd admin password:
   > kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d
 - Port-forward argocd,grafana and prometheus:
   > kubectl port-forward svc/argocd-server -n argocd 8080:443

   > kubectl port-forward svc/grafana -n monitoring 3100:80

   > kubectl port-forward svc/prometheus -n monitoring 9191:9090

 **Note**:
- Grafana Data Source Connection Prometheus server URL:
  http://prometheus.monitoring.svc.cluster.local:9090

   
