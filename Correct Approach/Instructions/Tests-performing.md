# Benchmarking - Setup for the tests performing

## Personal configuration
Replace with the IP of your VMs on GCP, it should be the same values as the Wursmeister-VM-setup.md file:

```
ZOOKEEPER-2: Ext: <ZOOKEEPER_EXTERNAL_IP> Int: <ZOOKEEPER_INTERNAL_IP> 

KAFKA-1: Ext: <KAFKA1_EXTERNAL_IP> Int: <KAFKA1_INTERNAL_IP>

KAFKA-2: Ext: <KAFKA2_EXTERNAL_IP> Int: <KAFKA2_INTERNAL_IP>

TOPIC: <topic_name> (choose yours)
```

## Consume Messages on kafka2 VM:
On the kafka2 VM, consume messages from the Kafka topic using, execute these commands one by one:
```bash
sudo docker exec -it kafka /bin/sh

cd opt/kafka/bin

kafka-console-consumer.sh --bootstrap-server <KAFKA1_EXTERNAL_IP>:9092,<KAFKA2_EXTERNAL_IP>:9092 --topic <topic_name> --from-beginning
```

## Produce Messages on kafka1 VM:
On the kafka1 VM, produce messages to the Kafka topic using the following command:

### Enter in the container and install nano and dstat
Execute these commands one by one:
```bash
sudo docker exec -it kafka /bin/sh

apt-get update

apt-get install nano

apt-get install dstat
```

### Create the script for message sending
Execute these commands one by one:
```bash
cd opt/kafka/bin

nano benchmark.sh
#Copy-paste the bash script from `benchmark.sh` file in Command tutorials folder of the repository.

chmod +x benchmark.sh
./benchmark.sh <topic_name> <KAFKA1_EXTERNAL_IP>:9092,<KAFKA2_EXTERNAL_IP>:9092
```

## Record the performance on kafka1 VM:
Execute these commands one by one:
```bash
sudo docker exec -it kafka /bin/sh

dstat -c -m
#Copy the information in a .txt file as in Data Parsing and use parser.py script.
```

## Parse the data
Go to `/Scripts` and run:
```
python .\parser.py .\Data\path-to-your-file\your-file.txt
```