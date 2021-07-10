#!/bin/sh
echo "Running Agent JMX Check for <AGENT_POD>: " $1
echo "\n"

kubectl exec -it $1 -- agent jmx list collected