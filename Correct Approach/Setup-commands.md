# Commands to run the cluster:

- Create the network if you already don't have one
docker network create my-network
### Build Zookeeper image:
In ./Zookeeper/
- docker build -t zookeeper-img .

### Run Zookeeper image:
- docker run -d -p 2181:2181 --network my-network --name my-zookeeper zookeeper-img


### Build Kafka image:
In ./Kafka/Client1:
- docker build -t kafka-img-1 .

In ./Kafka/Client2:
- docker build -t kafka-img-2 .

### Run Kafka image:
- docker run -d -p 9092:9092 --network my-network --name kafka-1 kafka-img-1
- docker run -d -p 9093:9093 --network my-network --name kafka-2 kafka-img-2

# Set-up the cluster:
- docker exec -it kafka-1 /bin/sh
- docker exec -it kafka-2 /bin/sh

kafka-1, kafka-2:
- cd opt/kafka

kafka-1:
- ./bin/kafka-topics.sh --create --zookeeper my-zookeeper:2181 --replication-factor 1 --partitions 1 --topic tema

kafka-2:
- ./bin/kafka-topics.sh --list --zookeeper my-zookeeper:2181
shoudl see 'tema'

kafka-1
- ./bin/kafka-console-producer.sh --broker-list kafka-1:9092 --topic tema

kafka-2:
- ./bin/kafka-console-consumer.sh --bootstrap-server kafka-2:9093 --topic tema --from-beginning


## Info sources:
https://dhruv-saksena.medium.com/dockerize-kafka-multi-node-cluster-8d8c5a6d8589
