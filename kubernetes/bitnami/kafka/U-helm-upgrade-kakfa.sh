#!/bin/sh
echo "Upgrading Bitnami Kafka .... \n"

helm upgrade bitnami-kafka bitnami/kafka -f ./values.yaml
