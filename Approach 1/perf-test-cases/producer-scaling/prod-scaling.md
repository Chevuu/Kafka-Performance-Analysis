Window 1:
- docker-compose -f docker-compose.yml up -d
- docker exec -it kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test-topic-prod
- cd /bin
- echo 'for i in $(seq 1 30); do
    message=$(dd if=/dev/urandom bs=256 count=1 | base64)
    echo "$message" | kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic-prod
    sleep 0.5
done' > base-script.sh
- chmod +x base-script.sh

Window 2:
- cd opt/kafka/bin
- ./base-script.sh

Window 1:
- ./base-script.sh

Window 3:
- docker exec -it kafka /bin/sh
- cd opt/kafka
- ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic-prod --from-beginning
