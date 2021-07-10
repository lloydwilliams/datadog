#!/bin/sh
echo "Installing Bitnami Kafka .... \n"

#kubectl create namespace kafka

#helm install bitnami-kafka bitnami/kafka -n kafka -f ./values.yaml
helm install bitnami-kafka bitnami/kafka -f ./values.yaml
#helm install bitnami-kafka bitnami/kafka


################
################
#Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:
#    bitnami-kafka.kafka.svc.cluster.local

#Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your cluster:
#    bitnami-kafka-0.bitnami-kafka-headless.kafka.svc.cluster.local:9092

#To create a pod that you can use as a Kafka client run the following commands:
#    kubectl run bitnami-kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.7.0-debian-10-r68 --namespace kafka --command -- sleep infinity
#    kubectl exec --tty -i bitnami-kafka-client --namespace kafka -- bash

#    PRODUCER:
#        kafka-console-producer.sh \
#            --broker-list bitnami-kafka-0.bitnami-kafka-headless.kafka.svc.cluster.local:9092 \
#            --topic test

#It's OK if it says leader not available
# run another
# kubectl exec --tty -i bitnami-kafka-client --namespace kafka -- bash

#    CONSUMER:
#        kafka-console-consumer.sh \
#            --bootstrap-server bitnami-kafka.kafka.svc.cluster.local:9092 \
#            --topic test
