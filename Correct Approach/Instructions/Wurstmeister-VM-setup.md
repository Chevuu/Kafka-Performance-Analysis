# Setup of the VMs with Kafka and Zookeeper containers


## Create 3 VMs (E3) on zone europe-west1-b with 4 cores and 8GB RAM in Google Cloud.

Name these machines zookeeper, kafka1, and kafka2.
Install Docker on Each VM:

Follow the official Docker installation instructions for Debian on each VM: https://docs.docker.com/engine/install/debian/#installation-methods

### Personal configuration
Once the VMs launched on GCP, replace these IP with yours :

```
ZOOKEEPER-2: Ext: <ZOOKEEPER_EXTERNAL_IP> Int: <ZOOKEEPER_INTERNAL_IP>

KAFKA-1: Ext: <KAFKA1_EXTERNAL_IP> Int: <KAFKA1_INTERNAL_IP>

KAFKA-2: Ext: <KAFKA2_EXTERNAL_IP> Int: <KAFKA2_INTERNAL_IP>

TOPIC: <topic_name> (choose yours)
```

## Configuration of the containers

### Run Zookeeper on Zookeeper VM:
On the zookeeper VM, run the following command to start Zookeeper using the Wurstmeister Zookeeper Docker image:
```bash
sudo docker run -d --name zookeeper -p 2181:2181 wurstmeister/zookeeper
```

### Run Kafka on kafka1 VM:
On the kafka1 VM, run the following command to start Kafka using the Wurstmeister Kafka Docker image with the specified environment variables:
```bash
sudo docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=<KAFKA1_EXTERNAL_IP> -e KAFKA_ADVERTISED_PORT=9092 -e KAFKA_BROKER_ID=1 -e KAFKA_ZOOKEEPER_CONNECT=<ZOOKEEPER_EXTERNAL_IP>:2181 wurstmeister/kafka
```

### Run Kafka on kafka2 VM:
On the kafka2 VM, run the following command to start Kafka using the Wurstmeister Kafka Docker image with the specified environment variables:
```bash
sudo docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=<KAFKA2_EXTERNAL_IP> -e KAFKA_ADVERTISED_PORT=9092 -e KAFKA_BROKER_ID=2 -e KAFKA_ZOOKEEPER_CONNECT=<ZOOKEEPER_IP>:2181 wurstmeister/kafka
```

### Create a Topic on kafka2 VM:
On the kafka2 VM, create a Kafka topic using the following command one by one:
```bash
sudo docker exec -it kafka /bin/sh

cd opt/kafka/bin

kafka-topics.sh --create --topic <topic_name> --partitions 1 --replication-factor 1 --zookeeper <ZOOKEEPER_IP>:2181
```

## Communication between the containers

### List the Topic on kafka1 or kafka2 VM:
On the kafka1 VM, you can list the Kafka topics using these commands one by one:
```bash
sudo docker exec -it kafka /bin/sh

cd opt/kafka/bin

kafka-topics.sh --list --zookeeper <ZOOKEEPER_IP>:2181
```

## Notes
You are now done with the configuration of the VMs unless you change the configuration of the VM itself.

If you decide to stop the VM to change the VM configuration, remember to update the IP in the `Personal configuration` section.