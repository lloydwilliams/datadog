#!/bin/sh
#kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-pod.yaml

kubectl apply -f envars.yaml

sleep 30

kubectl exec envar-demo -- printenv