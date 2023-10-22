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

## Performance testing
*Prerequisites* - first 6 steps

### producer
sudo docker run -it --rm ches/kafka kafka-producer-perf-test.sh --topic senz --throughput -1 --num-records 300000 --record-size 1024 --producer-props acks=all bootstrap.servers=<EXTERNAL_KAFKA1_IP>:9092,<EXTERNAL_KAFKA2_IP>:9092

Output should look like:
200629 records sent, 40125.8 records/sec (39.19 MB/sec), 651.5 ms avg latency, 830.0 max latency.
300000 records sent, 41413.583655 records/sec (40.44 MB/sec), 657.72 ms avg latency, 830.00 ms max latency, 675 ms 50th, 770 ms 95th, 800 ms 99th, 824 ms 99.9th.

I also want to say that numbers in the test above are random. I didn't really think closely about them.

### consumer
sudo docker run -it --rm ches/kafka kafka-consumer-perf-test.sh --topic senz --broker-list 35.241.180.5:9092,34.79.94.246:9092 --messages 3000000

Output should look like:
start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec
2023-10-22 19:49:28:577, 2023-10-22 19:49:33:610, 718.5498, 142.7677, 735795, 146194.1188