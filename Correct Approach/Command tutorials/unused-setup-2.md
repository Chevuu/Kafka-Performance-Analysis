1. Create 3 VMs on zone europe-west1-b with 4 cores and 8GB RAM in google cloud.
    - Name these machine zookeeper, kafka1 and kafka2
2. In each VM install docker using the following steps
    - https://docs.docker.com/engine/install/debian/#installation-methods
3. on zookeeper VM run zookeeper: sudo docker run -d --name zookeeper -p 2181:2181 jplock/zookeeper
4. On kafka1 VM and kafka2 VM run sudo docker run -d --name kafka -p 7203:7203 -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=<EXTERNAL_MACHINE_IP> -e ZOOKEEPER_IP=<EXTERNAL_ZOOKEEPER_IP> ches/kafka
5. Create a topic on kafka2 VM: sudo docker run --rm ches/kafka kafka-topics.sh --create --topic tema --replication-factor 1 --partitions 1 --zookeeper <EXTERNAL_ZOOKEEPER_IP>:2181
6. (Optional) List the topic on kafka1 VM: sudo docker run --rm ches/kafka kafka-topics.sh --list --zookeeper <EXTERNAL_ZOOKEEPER_IP>:2181
7. On kafka1 VM run the producer: sudo docker run -it --rm ches/kafka kafka-console-producer.sh --broker-list <EXTERNAL_KAFKA1_IP>:9092,<EXTERNAL_KAFKA2_IP>:9092 --topic tema
8. On kafka2 VM run the consumer: sudo docker run -it --rm ches/kafka kafka-console-consumer.sh --bootstrap-server <EXTERNAL_KAFKA1_IP>:9092,<EXTERNAL_KAFKA2_IP>:9092 --topic tema --from-beginning