# Plan stages

### Setup Kafka
This means that we need to figure out a way to have multiple kafka VMs communicate between each other. I haven't found a way to do that yet. I will ask the professor if we can do it in one VM but I'm not sure if that's the point. It seems also a bit wrong to use Docker inside Google Cloud so I'll also ask the professor what he thinks about that.

### Choose factors
We need to find 6 - 10 factors that affect performance as much as possible so that on monday we can ask the professor which (3 to 6) should we choose.
So far I am suggesting:
1. Number of brokers
2. Number of clusters
3. Number of producers (??)
4. background.threads
    - threads for background jobs
5. num.io.threads
    - threads that the server uses for processing requests
6. num.network.threads
    - threads that the server uses for receiving requests from the network and sending responses to the network

## Benchmark

Another way to get performance metrics is to use kafka-producer-perf-test.sh script and kafka-consumer-perf-test.sh script. Docker stats scripts were slow and very time consuming to run. also this time they might not even work.

### Run benchmark

After choosing the factors we will use we will use their default values or values of our choice to compute the benchmark and measure the performance. Benchmark performance will always be in top-left corner of our 2-factor-2-level tables.

### Testing

Yet to be planned out based on the factors.

### USL Formula

Recompute USL formula with new values.

## Pipeline

As mentioned in teachers feedback pipeline needs improvements. We need to perfectly describe what happens with the message inside kafka. Not what we do with the message.

### Finally

Using above, we will easily conclude what bottlenecks are and write the conclusion.
