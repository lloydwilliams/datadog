#!/bin/sh
kubectl config set-context --current --namespace datadog
helm delete my-datadog-operator