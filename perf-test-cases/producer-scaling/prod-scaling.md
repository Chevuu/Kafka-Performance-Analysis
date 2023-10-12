Do this for 1,2,4,8 produers

Window 1:
- docker-compose -f docker-compose.yml up -d
- docker exec -it kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test-topic
- cd /bin
- echo 'for i in $(seq 1 30); do
    echo "Message $i" | kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
    sleep 1
done' > base-script-prod.sh
- chmod +x base-script-prod.sh

Window 2:
- cd opt/kafka/bin
<<<<<<< HEAD
- ./base-script.sh
=======
- echo 'for i in $(seq 1 30); do
    echo "Message $i" | kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
    sleep 1
done' > base-script-prod.sh
- chmod +x base-script-prod.sh
>>>>>>> 39366d54babc9fdcf38b9422e2099413ec429d11

Window 1:
- ./base-script-prod.sh

<<<<<<< HEAD
=======
Window 2:
- ./base-script-prod.sh
.... do this in new windows to create as menay producers as you want.
>>>>>>> 39366d54babc9fdcf38b9422e2099413ec429d11

Window 3:
- docker exec -it kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning
