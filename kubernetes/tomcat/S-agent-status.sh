#!/bin/sh
echo "Running Agent Status Command for <AGENT_POD>: " $1
echo "\n"

kubectl exec -it $1 -- agent status
