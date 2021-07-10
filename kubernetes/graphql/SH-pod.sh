#!/bin/sh
echo "Connecting to pod <POD_NAME>: " $1
echo "\n"

kubectl exec -it $1 -- sh
