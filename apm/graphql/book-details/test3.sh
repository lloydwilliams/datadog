#!/bin/sh
curl --location --request POST 'http://localhost:8080/graphql' \
--header 'Content-Type: application/json' \
--data-raw '{"query":"query bookById ($id: ID) {\n    bookById (id: $id) {\n        id\n        name\n        pageCount\n        author {\n            id\n            firstName\n            lastName\n        }\n    }\n}","variables":{"id":"book-3"}}'
