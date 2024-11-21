#!/bin/bash
echo "Forwarding Prometheus and Grafana..."
kubectl port-forward svc/prometheus-kube-prometheus-prometheus -n monitoring 9090:9090 &
kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80 &
echo "Prometheus: http://localhost:9090"
echo "Grafana: http://localhost:3000"
