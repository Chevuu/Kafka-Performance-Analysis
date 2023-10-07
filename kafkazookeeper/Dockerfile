#extend the original ubuntu image
FROM ubuntu:22.04
#install ping, iproute and netcat
RUN apt-get update && apt-get install -y iputils-ping iproute2 netcat-traditional
#install jdk
RUN apt-get update && apt-get install openjdk-8-jre -y
#unzip kafka zip and rename at kafka
#ENV kafka_version=2.13-3.5.1
#ADD ./kafka_${kafka_version}.tgz ./
#CMD["tar -xvzf ./kafka_${kafka_version}.tgz ./"]
#RUN mv kafka_${kafka_version} kafka
#copy the starting script to the container image
#COPY entrypoint.sh /entrypoint.sh
#run the custom script using the "sh" shell
#CMD ["sh", "/entrypoint.sh"]

COPY kafka /kafka
CMD ["sh", "/kafka/bin/zookeeper-server-start.sh", "/kafka/config/zookeeper.properties"]
#CMD ["sh", "/kafka/bin/zookeeper-server-start.sh"]
