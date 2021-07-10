#!/bin/sh
echo "Starting Kafka Client to be a producer ... \n"

kubectl run bitnami-kafka-producer --restart='Never' --image docker.io/bitnami/kafka:2.7.0-debian-10-r68 --command -- sleep infinity

sleep 20

echo "Run: kafka-console-producer.sh --bootstrap-server bitnami-kafka.default.svc.cluster.local:9092 --topic test"

kubectl exec --tty -i bitnami-kafka-producer -- bash