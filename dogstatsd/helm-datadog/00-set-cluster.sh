#!/bin/sh

echo 'The current context is:'
kubectl config current-context 
sleep 2 
echo 'These are the available contexts:'
kubectl config get-contexts
sleep 2 
echo "Changing the context !! (edit this script as needed)"
kubectl config use-context lloyd-aks-dogstatsd-udp
sleep 2 
echo 'Now the current context is:'
kubectl config current-context
