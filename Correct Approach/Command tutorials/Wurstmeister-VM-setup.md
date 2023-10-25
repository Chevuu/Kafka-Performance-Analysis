ZOOKEEPER-2: Ext: 34.65.240.252 Int: 10.172.0.2 
KAFKA-1: Ext: 34.65.220.54 Int: 10.172.0.3
KAFKA-2: Ext: 34.65.181.63 Int: 10.172.0.3

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
sudo docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=34.65.220.54 -e KAFKA_ADVERTISED_PORT=9092 -e KAFKA_BROKER_ID=1 -e KAFKA_ZOOKEEPER_CONNECT=34.65.240.252:2181 wurstmeister/kafka
### Run Kafka on kafka2 VM:

On the kafka2 VM, run the following command to start Kafka using the Wurstmeister Kafka Docker image with the specified environment variables:
bash
sudo docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=34.65.181.63 -e KAFKA_ADVERTISED_PORT=9092 -e KAFKA_BROKER_ID=2 -e KAFKA_ZOOKEEPER_CONNECT=34.65.240.252:2181 wurstmeister/kafka
### Create a Topic on kafka2 VM:

On the kafka2 VM, create a Kafka topic using the following command:
bash
- sudo docker exec -it kafka /bin/sh
- cd opt/kafka/bin
- kafka-topics.sh --create --topic tema --partitions 1 --replication-factor 1 --zookeeper 34.65.240.252:2181
### (Optional) List the Topic on kafka1 or kafka2 VM:

On the kafka1 VM, you can list the Kafka topics using:
bash
- sudo docker exec -it kafka /bin/sh
- cd opt/kafka/bin
- kafka-topics.sh --list --zookeeper 34.65.240.252:2181
### Produce Messages on kafka1 VM:

On the kafka1 VM, produce messages to the Kafka topic using the following command:
bash
- sudo docker exec -it kafka /bin/sh
- cd opt/kafka/bin
- kafka-console-producer.sh --broker-list 34.65.220.54:9092,34.65.181.63:9092 --topic tema
### Consume Messages on kafka2 VM:

On the kafka2 VM, consume messages from the Kafka topic using:
bash
- sudo docker exec -it kafka /bin/sh
- cd opt/kafka/bin
- kafka-console-consumer.sh --bootstrap-server 34.65.220.54:9092,34.65.181.63:9092 --topic tema --from-beginning
