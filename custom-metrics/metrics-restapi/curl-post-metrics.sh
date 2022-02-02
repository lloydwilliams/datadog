curl --location --request POST 'https://api.datadoghq.com/api/v1/series?api_key=PUT_API_KEY_HERE&application_key=PUT_APP_KEY_HERE' \
--header 'Content-Type: application/json' \
--data-raw '{
    "series": [
        {
            "metric": "lloyd.api.metric.5",
            "points": [
                [
                    "1643673699",
                    "1234.57"
                ]
            ],
            "host": "HOSTNAME",
            "interval": null,
            "tags": [
                "test:five",
                "year:2022"
            ],
            "type": "gauge"
        }
    ]
}'