#!/bin/bash
echo "Starting Minikube..."
minikube start --memory=4096 --cpus=2
minikube addons enable ingress
minikube addons enable metrics-server
