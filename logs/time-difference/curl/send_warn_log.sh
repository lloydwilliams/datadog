#!/bin/sh
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
    "status": "WARN",
    "message": "2021-07-16 09:09:19 WARN Account: A42615897 Date1: 2021-07-10 08:05:19 and Date2: 2021-07-10 08:51:11"
}'