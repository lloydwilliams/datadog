#!/bin/sh
#https://docs.datadoghq.com/agent/cluster_agent/clusterchecks/?tab=helm#dispatching-logic-in-the-cluster-agent
# kubectl exec <CLUSTER_AGENT_POD_NAME> agent clusterchecks
echo 'The datadog agent cluster agent is:'
kubectl get pods | grep datadog-agent-cluster-agent

# echo 'see: https://docs.datadoghq.com/agent/cluster_agent/clusterchecksrunner/?tab=helm'
echo '=== cluster agent clusterchecks ==='
kubectl exec datadog-agent-cluster-agent-c69d658b6-s4qgv -- agent clusterchecks

sleep 5
echo ''
echo '=== agent status ==='
# agent status
# kubectl exec -it <AGENT_POD_NAME> agent status

# kubectl exec -it datadog-agent-lnplf -- agent status