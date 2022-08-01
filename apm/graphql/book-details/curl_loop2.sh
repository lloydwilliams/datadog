#!/bin/sh
for i in {1..50}
do
  curl 'http://localhost:8080/graphql' -H 'Accept-Encoding: gzip, deflate, br' \
     -H 'Content-Type: application/json' -H 'Accept: application/json' \
     -H 'Connection: keep-alive' -H 'DNT: 1' \
     -H 'Origin: file://' --data-binary '{"query":"{\n  bookById(id: \"book-2\"){\n    id\n    name\n    pageCount\n    author {\n      firstName\n      lastName\n    }\n  }\n}"}' --compressed
    sleep 4
done 