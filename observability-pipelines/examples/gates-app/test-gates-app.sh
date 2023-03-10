#!/bin/sh


MINWAIT=2
MAXWAIT=10
# sleep $((MINWAIT+RANDOM % (MAXWAIT-MINWAIT)))

# In a 'read' statement (also a type of assignment):
echo -n "Enter the number of times."
read a
echo "The value of \"a\" is now $a."

START=1
END=a
## save $START, just in case if we need it later ##
i=$START
while [[ $i -le $END ]]
do
    echo "$i"
    ((i = i + 1))

curl --location --request POST 'localhost:8080/gate' \
--header 'Content-Type: application/json' \
--data-raw '{
    "gatenum": "8",
    "location": "Calgary",
    "identity": "xyz",
    "direction": "IN"
}'

sleep $((MINWAIT+RANDOM % (MAXWAIT-MINWAIT)))
echo ""

curl --location --request POST 'localhost:8080/gate' \
--header 'Content-Type: application/json' \
--data-raw '{
    "gatenum": "22",
    "location": "Toronto",
    "identity": "lmo",
    "direction": "IN"
}'

sleep $((MINWAIT+RANDOM % (MAXWAIT-MINWAIT)))
echo ""

curl --location --request POST 'localhost:8080/gate' \
--header 'Content-Type: application/json' \
--data-raw '{
    "gatenum": "122",
    "location": "Montreal",
    "identity": "pqr",
    "direction": "IN"
}'

sleep $((MINWAIT+RANDOM % (MAXWAIT-MINWAIT)))
echo ""

curl --location --request POST 'localhost:8080/gate' \
--header 'Content-Type: application/json' \
--data-raw '{
    "gatenum": "22",
    "location": "Toronto",    
    "identity": "lmo",
    "direction": "OUT"
}'

sleep $((MINWAIT+RANDOM % (MAXWAIT-MINWAIT)))
echo ""

curl --location --request POST 'localhost:8080/gate' \
--header 'Content-Type: application/json' \
--data-raw '{
    "gatenum": "8",
    "location": "Calgary",
    "identity": "xyz",
    "direction": "OUT"
}'

sleep $((MINWAIT+RANDOM % (MAXWAIT-MINWAIT)))
echo ""

curl --location --request POST 'localhost:8080/gate' \
--header 'Content-Type: application/json' \
--data-raw '{
    "gatenum": "122",
    "location": "Montreal",
    "identity": "pqr",
    "direction": "OUT"
}'

echo ""
done