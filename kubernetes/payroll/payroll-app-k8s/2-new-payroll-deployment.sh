#!/bin/sh
kubectl config set-context --current --namespace payroll
kubectl apply -f new-payroll-deployment.yaml