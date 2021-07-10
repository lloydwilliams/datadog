#!/bin/bash
echo "Connecting to pod <AGENT_POD>: " $1
echo "\n"

kubectl exec -it $1 -- sh
