#!/bin/bash
kubectl config set-context --current --namespace default
#kubectl delete pod <AGENT POD NAME>
#kubectl exec -it $1 agent status
kubectl delete pod $1