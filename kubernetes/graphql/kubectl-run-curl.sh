#!/bin/sh
kubectl run curl --image=radial/busyboxplus:curl -i --tty

curl 'http://10.204.13.171:8080/graphql' -H 'Accept-Encoding: gzip, deflate, br' \
   -H 'Content-Type: application/json' -H 'Accept: application/json' \
   -H 'Connection: keep-alive' -H 'DNT: 1' \
   -H 'Origin: file://' --data-binary '{"query":"{\n  bookById(id: \"book-1\"){\n    id\n    name\n    pageCount\n    author {\n      firstName\n      lastName\n    }\n  }\n}"}' --compressed