#!/bin/bash
kubectl annotate pods zookeeper-0 ad.datadoghq.com/zk.check_names='["zk"]'
kubectl annotate pods zookeeper-0 ad.datadoghq.com/zk.init_configs='[{}]'
kubectl annotate pods zookeeper-0 ad.datadoghq.com/zk.instances='[{"host": "%%host%%", "port": "2181"}]'  

kubectl annotate pods zookeeper-1 ad.datadoghq.com/zk.check_names='["zk"]'
kubectl annotate pods zookeeper-1 ad.datadoghq.com/zk.init_configs='[{}]'
kubectl annotate pods zookeeper-1 ad.datadoghq.com/zk.instances='[{"host": "%%host%%", "port": "2181"}]'  

kubectl annotate pods zookeeper-2 ad.datadoghq.com/zk.check_names='["zk"]'
kubectl annotate pods zookeeper-2 ad.datadoghq.com/zk.init_configs='[{}]'
kubectl annotate pods zookeeper-2 ad.datadoghq.com/zk.instances='[{"host": "%%host%%", "port": "2181"}]'  

kubectl annotate pods kafka-0 ad.datadoghq.com/kafka.check_names='["kafka"]'
kubectl annotate pods kafka-0 ad.datadoghq.com/kafka.init_configs='[{"is_jmx": true, "collect_default_metrics": true}]'
kubectl annotate pods kafka-0 ad.datadoghq.com/kafka.instances='[{"host": "%%host%%","port":"7203"}]'

kubectl annotate pods kafka-1 ad.datadoghq.com/kafka.check_names='["kafka"]'
kubectl annotate pods kafka-1 ad.datadoghq.com/kafka.init_configs='[{"is_jmx": true, "collect_default_metrics": true}]'
kubectl annotate pods kafka-1 ad.datadoghq.com/kafka.instances='[{"host": "%%host%%","port":"7203"}]'

kubectl annotate pods kafka-2 ad.datadoghq.com/kafka.check_names='["kafka"]'
kubectl annotate pods kafka-2 ad.datadoghq.com/kafka.init_configs='[{"is_jmx": true, "collect_default_metrics": true}]'
kubectl annotate pods kafka-2 ad.datadoghq.com/kafka.instances='[{"host": "%%host%%","port":"7203"}]'
