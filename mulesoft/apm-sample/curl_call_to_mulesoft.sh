#!/bin/sh
curl --location --request POST 'localhost:9501/mulesoft' \
--header 'content-type: application/json' \
--data-raw '{
    "name": "Lloyd Williams",
    "role": "Enterprise Sales Engineer"
}
'
