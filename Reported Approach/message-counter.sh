#!/bin/bash

# Set the initial count to 0
count=0

# Start the Kafka consumer in the background
./bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test --from-beginning | while read message; do
  # Increment the count for each received message
  ((count++))
  # Extract the first 3 letters of the message
  # Output the count and the first 3 letters of the message
  echo "Count: $count"
done