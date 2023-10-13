- docker-compose -f docker-compose.yml up -d
- docker exec -it Kafka /bin/sh
- cd opt/kafka
<<<<<<< HEAD
- ./bin/kafka-topics.sh --create --zookeeper my-zookeeper:2181 --replication-factor 1 --partitions 1 --topic test
- ./bin/kafka-topics.sh --list --zookeeper my-zookeeper:2181
- ./bin/kafka-console-producer.sh --broker-list kafka-1:9092 --topic test
=======
- ./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test
- ./bin/kafka-topics.sh --list --zookeeper zookeeper:2181
- ./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
>>>>>>> 39c6fff416a014913ad9a2533976af83e7e8bf38
Now a '>' will show and you can write messages. Press Enter to write a new one or Ctrl + c to exit.
Now open a new terminal window and do:
- docker exec -it Kafka /bin/sh
- cd opt/kafka
<<<<<<< HEAD
- ./bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test --from-beginning
=======
- ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
>>>>>>> 39c6fff416a014913ad9a2533976af83e7e8bf38
