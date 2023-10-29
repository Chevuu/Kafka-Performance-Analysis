#!/bin/bash

#Check the topic
if [ $# -ne 2 ]; then
    echo "Usage: $0 <kafka_topic> <broker_list>"
    exit 1
fi

kafka_topic="$1"
kafka_brokers="$2"

# Initialization - Message of 256KB for 30 seconds
message=$(dd if=/dev/urandom bs=256 count=1 | base64)
message_sent=""
end_time=$((SECONDS + 30))

# Send messages
for ((message_counter = 1; SECONDS < end_time; message_counter++)); do
    message_sent+="$message_counter: $message"$'\n'
done

# Print messages sent
echo -n "$message_sent" | kafka-console-producer.sh --broker-list $kafka_brokers --topic $kafka_topic
