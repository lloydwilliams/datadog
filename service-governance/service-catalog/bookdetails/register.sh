#!/bin/sh

curl -X POST --data-binary @bookdetails.yaml \
  -H "Content-type: text/x-yaml" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  https://api.datadoghq.com/api/v2/services/definitions