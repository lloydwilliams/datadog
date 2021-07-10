#!/bin/sh
echo "Upgrading Confluent Operator .... \n"

helm upgrade confluent-operator confluentinc/confluent-for-kubernetes -f ./confluent-for-k8s-values.yaml