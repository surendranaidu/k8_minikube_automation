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
