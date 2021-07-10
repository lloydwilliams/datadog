#!/bin/sh
echo "Running Agent Config Check for <AGENT_POD>: " $1
echo "\n"

kubectl exec -it $1 -- agent configcheck
