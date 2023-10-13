# Tutorial for Producer scaling performance measure

## Create 1 Consumers
Window 1:
Now let's scale amount of consumers, do this for 1 consumers:
- docker exec -it Kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning

## Create the sending message script
Window 2:
- docker-compose -f docker-compose.yml up -d
- docker exec -it Kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test-topic
- cd /bin
- echo 'for i in $(seq 1 30); do
    message=$(dd if=/dev/urandom bs=256 count=1 | base64)
    echo "$message" | kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
    sleep 0.2
done' > base-script.sh
- chmod +x base-script.sh

## Create the 10 producers
Window 3..12:
Launch the script as the 10 producers :
- docker-compose -f docker-compose.yml up -d
- docker exec -it Kafka /bin/sh
- cd opt/kafka/bin
- ./base-script.sh

## Catch the performance 
Window n+1:
Now in window n+1 do:
- docker stats Kafka
Observe the performance
