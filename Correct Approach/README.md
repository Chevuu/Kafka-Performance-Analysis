# Setup

## Create image & container
### Zookeeper
In directory /"Correct Approach"/Zookeeper run :
- docker build -t  zookeeper-image .
- docker run -d -p 2181:2181 --name zookeeperTest -e ZOOKEEPER_CLIENT_PORT=2181 zookeeper-image

### Kafka
In directory /"Correct Approach"/Kafka run :
- docker build -t  kafka-image .

- docker run -d --name kafkaTest1 --link zookeeperTest:zookeeper -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafkaTest1:9092 -e KAFKA_LISTENERS=PLAINTEXT://:9092 -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 kafka-image

- docker run -d --name kafkaTest2 --link zookeeperTest:zookeeper -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafkaTest2:9092 -e KAFKA_LISTENERS=PLAINTEXT://:9092 -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 kafka-image

### Client & Producer Setup

#### Client Listening
Window 1 :
- docker exec -it kafkaTest1 /bin/bash

In `/opt/kafka/bin` directory :
Create a topic with 2 replication-factor :
- kafka-topics.sh --create --topic topic-test --partitions 1 --replication-factor 2 --zookeeper zookeeperTest:2181

Check its creation :
- kafka-topics.sh --list --zookeeper zookeeperTest:2181

Listen to the topic (got error for the moment) :
- kafka-console-consumer.sh --topic topic-test --bootstrap-server localhost:9092 --from-beginning

#### Producer Sending
Window 2 :
- docker exec -it kafkaTest2 /bin/bash

In `/opt/kafka/bin` directory :
Check the topic :
- kafka-topics.sh --list --zookeeper zookeeperTest:2181

Send message to the topic (got error for the moment) :
- kafka-console-producer.sh --topic topic-test --bootstrap-server kafkaTest1:9092