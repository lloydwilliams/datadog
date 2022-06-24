#!/bin/sh
kubectl config set-context --current --namespace payroll
kubectl apply -f payroll-deployment.yaml