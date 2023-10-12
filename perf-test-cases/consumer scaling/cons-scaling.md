Do this for 1,2,4,8 produers

Window 1:
- docker-compose -f docker-compose.yml up -d
- docker exec -it Kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test-topic
- cd /bin
- echo 'for i in $(seq 1 30); do
    message=$(dd if=/dev/urandom bs=256 count=1 | base64)
    echo "$message" | kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
    sleep 0.5
done' > base-script-cons.sh
- chmod +x base-script-cons.sh

Now let's scale amount of consumers, do this for 1, 2, 4, 8 consumers:
Window 2..3..4..5..6..7..8 (as much as you need):
- docker exec -it Kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning


Window 1:
- ./base-script-cons.sh

now in window n+1 do:
- docker stats
observe performance
