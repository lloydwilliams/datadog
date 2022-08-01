This is a graphql sample that runs on an embedded tomcat

This came from:
https://www.graphql-java.com/tutorials/getting-started-with-spring-boot/

The URL is:
http://localhost:8080/graphql

You can put this in GraphQL Playground:

{
  bookById(id: "book-1"){
    id
    name
    pageCount
    author {
      firstName
      lastName
    }
  }
}

{
  bookById(id: "book-2"){
    id
    name
    pageCount
    author {
      firstName
      lastName
    }
  }
}

Test using curl:

curl 'http://localhost:8080/graphql' -H 'Accept-Encoding: gzip, deflate, br' \
   -H 'Content-Type: application/json' -H 'Accept: application/json' \
   -H 'Connection: keep-alive' -H 'DNT: 1' \
   -H 'Origin: file://' --data-binary '{"query":"{\n  bookById(id: \"book-1\"){\n    id\n    name\n    pageCount\n    author {\n      firstName\n      lastName\n    }\n  }\n}"}' --compressed
   
   
curl 'http://localhost:8080/graphql' -H 'Accept-Encoding: gzip, deflate, br' \
   -H 'Content-Type: application/json' -H 'Accept: application/json' \
   -H 'Connection: keep-alive' -H 'DNT: 1' \
   -H 'Origin: file://' --data-binary '{"query":"{\n  bookById(id: \"book-2\"){\n    id\n    name\n    pageCount\n    author {\n      firstName\n      lastName\n    }\n  }\n}"}' --compressed