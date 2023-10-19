# Use the official Apache Kafka image as the base image
FROM wurstmeister/kafka

# Expose Kafka port
EXPOSE 9093

# Set environment variables for Kafka configuration
ENV KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka-2:9093
ENV KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9093

# Set other Kafka environment variables if needed
ENV KAFKA_BROKER_ID=2
ENV KAFKA_ZOOKEEPER_CONNECT=my-zookeeper:2181
