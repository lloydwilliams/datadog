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
    "status": "ERROR",
    "message": "2021-07-16 09:09:19 ERROR Account: EA0615897 Date1: 2021-07-05 19:12:19 and Date2: 2021-07-06 11:59:31"
}'