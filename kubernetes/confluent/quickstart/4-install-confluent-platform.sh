#!/bin/bash
echo installing confluent platform

kubectl apply -f confluent-platform.yaml
#kubectl apply -f https://raw.githubusercontent.com/confluentinc/confluent-kubernetes-examples/master/quickstart-deploy/confluent-platform.yaml


#installing confluent platform
#---------------------------------
#zookeeper.platform.confluent.io/zookeeper created
#kafka.platform.confluent.io/kafka created
#connect.platform.confluent.io/connect created
#ksqldb.platform.confluent.io/ksqldb created
#controlcenter.platform.confluent.io/controlcenter created
#schemaregistry.platform.confluent.io/schemaregistry created

