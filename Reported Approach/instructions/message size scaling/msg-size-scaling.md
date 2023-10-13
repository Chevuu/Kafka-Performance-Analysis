# Tutorial for Message Size scaling performance measure

## Create 1 Consumers
Window 1:
Now let's scale amount of consumers, do this for 1 consumers:
- docker exec -it Kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning

## Create 1 Producer
Window 2:
- docker-compose -f docker-compose.yml up -d
- docker exec -it Kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test-topic
- cd /bin
- echo 'for i in $(seq 1 30); do
    message=$(dd if=/dev/urandom bs=4 count=1 | base64)
    echo "$message" | kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
    sleep 0.2
done' > base-script.sh
- chmod +x base-script.sh
- ./base-script.sh

## Catch the performance 
Window n+1:
Now in window n+1 do:
- docker stats Kafka
Observe the performance

## Scale up the Message Size
- nano base-script.sh
Modify the bs parameter :
4, 64, 256, 1024, 4096, 32768, 1048576, 33554432