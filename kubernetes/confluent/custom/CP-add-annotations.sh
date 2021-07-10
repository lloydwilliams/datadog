#!/bin/bash
kubectl annotate pods connect-0 ad.datadoghq.com/confluent_platform.check_names='["confluent_platform"]'
kubectl annotate pods connect-0 ad.datadoghq.com/confluent_platform.init_configs='[{"is_jmx": true, "collect_default_metrics": true}]'
kubectl annotate pods connect-0 ad.datadoghq.com/confluent_platform.instances='[{"host": "%%host%%","port":"7203"}]'

kubectl annotate pods connect-1 ad.datadoghq.com/confluent_platform.check_names='["confluent_platform"]'
kubectl annotate pods connect-1 ad.datadoghq.com/confluent_platform.init_configs='[{"is_jmx": true, "collect_default_metrics": true}]'
kubectl annotate pods connect-1 ad.datadoghq.com/confluent_platform.instances='[{"host": "%%host%%","port":"7203"}]'

#kubectl desribe connect-0
#kubectl desribe connect-1

# kubectl annotate [--overwrite] (-f FILENAME | TYPE NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--resource-version=version]
# kubectl annotate --overwrite pods foo description='my frontend running nginx'

# https://ansilh.com/04-labels_and_annotations/02-annotations/
# Remove annotation
# Use same annotate command and mention only key with a dash (-) at the end of the key . Below command will remove the annotation
# kubectl annotate pod coffee-app url-

