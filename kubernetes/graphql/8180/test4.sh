#!/bin/sh
curl 'http://localhost:8180/graphql' -H 'Accept-Encoding: gzip, deflate, br' \
   -H 'Content-Type: application/json' -H 'Accept: application/json' \
   -H 'Connection: keep-alive' -H 'DNT: 1' \
   -H 'Origin: file://' --data-binary '{"query":"{\n  bookById(id: \"book-4\"){\n    id\n    name\n    pageCount\n    author {\n      firstName\n      lastName\n    }\n  }\n}"}' --compressed