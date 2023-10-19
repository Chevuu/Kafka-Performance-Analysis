# Image
FROM wurstmeister/kafka

# Kafka instance 1
ENV KAFKA_ADVERTISED_LISTENERS1=PLAINTEXT://kafkaTest1:9092
ENV KAFKA_LISTENERS1=PLAINTEXT://:9092

<<<<<<< HEAD:Correct Approach/Kafka/Dockerfile
# Kafka instance 2
ENV KAFKA_ADVERTISED_LISTENERS2=PLAINTEXT://kafkaTest2:9092
ENV KAFKA_LISTENERS2=PLAINTEXT://:9093
=======
# Set environment variables for Kafka configuration
ENV KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka-1:9092
ENV KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092
>>>>>>> ba2d9276bdab6efc3833020ad58063351884a871:Correct Approach/Kafka/Client1/Dockerfile

# Both instance
ENV KAFKA_ZOOKEEPER_CONNECT=zookeeperTest:2181