#!/bin/sh
for i in {1..100}
do
curl --location --request POST 'https://http-intake.logs.datadoghq.com/v1/input/' \
--header 'Content-Type: application/json' \
--header 'DD-API-KEY: <<INSERT_YOUR_API_KEY_HERE>>' \
--data-raw '{
    "ddsource": "postman",
    "ddtags": "version:1.2",
    "hostname": "myhostname",
    "organization": "datadog",
    "env": "dev",
    "service": "postman",
    "status": "INFO",
    "message": "2021-07-16 09:09:19 INFO Account: A51415897 Date1: 2021-07-10 08:05:19 and Date2: 2021-07-10 10:21:43"
}'
sleep 2
done