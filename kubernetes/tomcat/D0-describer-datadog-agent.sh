#!/bin/sh
echo "Describe daemonset: \n"
kubectl get daemonset 
kubectl describe daemonset datadog-agent
