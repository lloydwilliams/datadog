#!/bin/bash
echo "Usage Example: ./SSH-agent-pod.sh datadog-agent-7l8bm 123456"
echo "\n"
kubectl config set-context --current --namespace default
kubectl exec -it $1 -- bash