#!/bin/sh
kubectl config set-context --current --namespace datadog
helm uninstall datadog-agent