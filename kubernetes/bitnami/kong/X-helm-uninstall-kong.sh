#!/bin/sh
echo "Uninstalling Bitnami Kong .... \n"

## kubectl create namespace kong

helm -n kong uninstall bitnami/kong
