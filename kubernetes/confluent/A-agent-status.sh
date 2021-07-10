#!/bin/bash
kubectl config set-context --current --namespace default
kubectl exec -it $1 agent status
