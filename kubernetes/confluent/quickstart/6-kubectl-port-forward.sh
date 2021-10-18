#!/bin/sh
echo portforwarding 9021 for control-center
kubectl port-forward controlcenter-0 9021:9021