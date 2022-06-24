#!/bin/sh
# https://docs.datadoghq.com/agent/cluster_agent/setup/?tab=helm#verification
kubectl get pods | grep agent