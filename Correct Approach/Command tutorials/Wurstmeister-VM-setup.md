ZOOKEEPER-2: Ext: <ZOOKEEPER_IP> Int: 10.172.0.2 
KAFKA-1: Ext: <KAFKA1_EXTERNAL_IP> Int: 10.172.0.3
KAFKA-2: Ext: <KAFKA2_EXTERNAL_IP> Int: 10.172.0.3

### Create 3 VMs on zone europe-west1-b with 4 cores and 8GB RAM in Google Cloud.

Name these machines zookeeper, kafka1, and kafka2.
Install Docker on Each VM:

Follow the official Docker installation instructions for Debian on each VM: https://docs.docker.com/engine/install/debian/#installation-methods
### Run Zookeeper on Zookeeper VM:

On the zookeeper VM, run the following command to start Zookeeper using the Wurstmeister Zookeeper Docker image:
bash
sudo docker run -d --name zookeeper -p 2181:2181 wurstmeister/zookeeper
### Run Kafka on kafka1 VM:

On the kafka1 VM, run the following command to start Kafka using the Wurstmeister Kafka Docker image with the specified environment variables:
bash
sudo docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=<KAFKA1_EXTERNAL_IP> -e KAFKA_ADVERTISED_PORT=9092 -e KAFKA_BROKER_ID=1 -e KAFKA_ZOOKEEPER_CONNECT=<ZOOKEEPER_EXTERNAL_IP></ZOOKEEPER_IP>:2181 wurstmeister/kafka
### Run Kafka on kafka2 VM:

On the kafka2 VM, run the following command to start Kafka using the Wurstmeister Kafka Docker image with the specified environment variables:
bash
sudo docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=<KAFKA2_EXTERNAL_IP> -e KAFKA_ADVERTISED_PORT=9092 -e KAFKA_BROKER_ID=2 -e KAFKA_ZOOKEEPER_CONNECT=<ZOOKEEPER_IP>:2181 wurstmeister/kafka
### Create a Topic on kafka2 VM:

On the kafka2 VM, create a Kafka topic using the following command:
bash
- sudo docker exec -it kafka /bin/sh
- cd opt/kafka/bin
- kafka-topics.sh --create --topic tema --partitions 1 --replication-factor 1 --zookeeper <ZOOKEEPER_IP>:2181
### (Optional) List the Topic on kafka1 or kafka2 VM:

On the kafka1 VM, you can list the Kafka topics using:
bash
- sudo docker exec -it kafka /bin/sh
- cd opt/kafka/bin
- kafka-topics.sh --list --zookeeper <ZOOKEEPER_IP>:2181
### Produce Messages on kafka1 VM:

On the kafka1 VM, produce messages to the Kafka topic using the following command:
bash
- sudo docker exec -it kafka /bin/sh
- cd opt/kafka/bin
- kafka-console-producer.sh --broker-list <KAFKA1_EXTERNAL_IP>:9092,<KAFKA2_EXTERNAL_IP>:9092 --topic tema
### Consume Messages on kafka2 VM:

On the kafka2 VM, consume messages from the Kafka topic using:
bash
- sudo docker exec -it kafka /bin/sh
- cd opt/kafka/bin
- kafka-console-consumer.sh --bootstrap-server <KAFKA1_EXTERNAL_IP>:9092,<KAFKA2_EXTERNAL_IP>:9092 --topic tema --from-beginning


## Benchmarking
open two kafka1 windows and one kafka2 window

On kafka window start consuming. You never have to turn that off.

On kafka1 window 1:
- sudo docker exec -it kafka /bin/sh
- cd opt/fafka/bin
- Do this:
```bash
echo "#!/bin/bash

# Check if the topic argument is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <kafka_topic> <broker_list>"
    exit 1
fi

kafka_topic="$1"
kafka_brokers="$2"

# Generate a 256KB message
message=$(dd if=/dev/urandom bs=256 count=1 | base64)

# Run the Kafka producer for 30 seconds
end_time=$((SECONDS + 30))

while [ $SECONDS -lt $end_time ]; do
    echo "$message" | kafka-console-producer.sh --broker-list $kafka_brokers --topic $kafka_topic
done
" > benchmark.sh
```
- chmod +x benchmark.sh
- ./benchmark.sh <topic_name> 

In another window:
run  `dstat -c -m`
Copy that into a text file as in Data Parsing and use parser script.