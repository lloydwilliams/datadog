#!/bin/sh
echo "Starting Kafka Client to be a consumer ... \n"

kubectl run bitnami-kafka-consumer --restart='Never' --image docker.io/bitnami/kafka:2.7.0-debian-10-r68 --command -- sleep infinity

sleep 20

echo "Run: kafka-console-consumer.sh --bootstrap-server bitnami-kafka.default.svc.cluster.local:9092 --topic test"

kubectl exec --tty -i bitnami-kafka-consumer -- bash
