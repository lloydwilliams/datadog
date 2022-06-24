#!/bin/sh
#run 'docker images' to get the IMAGE ID
echo 'docker-tag.sh <image_id>'
docker tag $1 lloydwilliams/payroll:latest