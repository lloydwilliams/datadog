#!/bin/sh
curl -X POST \
-H "Content-Type: application/json" \
-d '{"query":"{\n  bookById(id: \"book-2\"){\n    id\n    name\n    pageCount\n    author {\n      firstName\n      lastName\n    }\n  }\n}"}' \
http://127.0.0.1:8180/graphql