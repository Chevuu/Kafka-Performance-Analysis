# Stage 2

## Organization

### Config folder
In this file you will find the configuration we used for Kafka and Zookeeper. These configuration allowed us to properly link all the instances between them.
No need to lunch the Dockerfile, the instructions for the VMs setup will be discussed in Instruction folder section.

### Data folder
In this folder, you will find all the data we got from our performance test. We separated the file from the global tests and the tests for the scalability calculation.

### Instruction folder
In this folder, you will find important files which will help to setup the VMs with Kafka and Zookeeper to launch properly the tests.
Here is the description of the files :
- Setup of the VMs | Wurstmeister-VM-setup.md
- Preparation for the tests | Test-performing.md

### Script folder
In this folder, we stored the scripts we used to send messages for our tests and the script to parse the data.
The parsing script allowed us to properly analyze the data.