#Fetch latest version of newly added charts: 
mkdir -p CFK
helm pull confluentinc/confluent-for-kubernetes --untar --untardir=CFK --namespace confluent

#Edit the <CFK-home>/values.yaml file to customize the CFK configuration.

helm upgrade --install confluent-operator \
  confluentinc/confluent-for-kubernetes \
  --values CFK/values.yaml \
  --namespace confluent

# https://confluent-for-kubernetes.s3-us-west-1.amazonaws.com/confluent-for-kubernetes-2.0.1.tar.gz
# cd CFK 
#helm upgrade --install confluent-operator ./confluent-for-kubernetes --namespace confluent