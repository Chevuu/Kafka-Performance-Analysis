### Benchmark
1 consumer 1 producer
And consumer running this:
#!/bin/bash
for i in $(seq 1 30); do
    message=$(dd if=/dev/urandom bs=256 count=1 | base64)
    echo "$message" | kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
    sleep 0.2
done

## Parameters
These are the parameters we'll be scaling to analyze our system.
- number of producers
- number of consumers
- frequency of messages
- size of messages

## Plan
In perf-test-cases folder you can find a plan for scaling consumers and producers. When observing docker stats, note down CPU usage and memory usage and any other information you find important. Later we'll plot some graphs and try to explain the information we got. You can also find a series of commands you have to put into your terminal in order to run the software.