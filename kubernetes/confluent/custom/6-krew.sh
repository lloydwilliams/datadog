#https://docs.confluent.io/operator/current/co-deploy-cfk.html#install-confluent-plugin-using-krew
#Install Krew as described in Krew User Guide.
#cd kubectl-plugin\confluent-for-kubernetes-2.0.1-20210609\kubectl-plugin

cd kubectl-plugin

kubectl krew install \
  --manifest=confluent-platform.yaml \
  --archive=kubectl-confluent-darwin-amd64.tar.gz