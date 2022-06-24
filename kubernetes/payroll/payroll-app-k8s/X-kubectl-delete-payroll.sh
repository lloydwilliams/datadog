#!/bin/sh
kubectl config set-context --current --namespace payroll
kubectl delete -f payroll-deployment.yaml
#kubectl delete pods,services -l name=payroll-deployment
kubectl delete service payroll-deployment
