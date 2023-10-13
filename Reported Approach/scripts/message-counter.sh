#!/bin/bash

count=0

./bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test --from-beginning | while read message; do
  ((count++))
  echo "Count: $count"
done