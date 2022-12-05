#!/bin/sh
kubectl config set-context --current --namespace datadog
helm delete datadog-agent