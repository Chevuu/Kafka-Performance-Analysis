param (
    [int]$numProducers = 1
)

function StartKafkaProducer {
    Write-Host "StartKafkaProducer method entered"
    try {
        Write-Host "StartKafkaProducer: Starting Kafka producer..."
        docker exec -it kafka /bin/sh -c 'cd /opt/kafka && echo "for i in $(seq 1 30); do
        message=$(dd if=/dev/urandom bs=256 count=1 | base64)
        echo \"$message\" | ./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic-prod
        sleep 0.5
    done" > /bin/base-script.sh && chmod +x /bin/base-script.sh && /bin/base-script.sh'
        Write-Host "StartKafkaProducer: Kafka producer execution completed successfully."
    } catch {
        Write-Host "StartKafkaProducer: Error - $_"
    }
}


function StartKafkaConsumer {
    Write-Host "StartKafkaConsumer method entered"
    try {
        Write-Host "StartKafkaConsumer: Starting Kafka consumer..."
        docker exec -it kafka /bin/sh -c "cd /opt/kafka && ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic-prod --from-beginning"
        Write-Host "StartKafkaConsumer: Kafka consumer execution completed successfully."
    } catch {
        Write-Host "StartKafkaConsumer: Error - $_"
    }
}

function CollectDockerStats {
    Write-Host "StartKafkaConsumer method entered"
    try {
        Write-Host "CollectDockerStats: Collecting Docker stats..."
        $outputFile = "docker_stats_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
        docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}" >> $outputFile
        Write-Host "CollectDockerStats: Docker stats collection completed successfully."
    } catch {
        Write-Host "CollectDockerStats: Error - $_"
    }
}

for ($i = 1; $i -le $numProducers; $i++) {
    Write-Host "Starting producer $i."
    Start-Job -ScriptBlock { StartKafkaProducer }
}

Start-Job -ScriptBlock { StartKafkaConsumer }

Start-Job -ScriptBlock {
    $script:collecting = $true
    $i = 0
    while ($script:collecting) {
        $i++
        CollectDockerStats
        Write-Host "Collecting Docker Stats for $i seconds"
        Start-Sleep -Seconds 1
    }
}

Start-Sleep -Seconds 30

Get-Job | Stop-Job
Get-Job | Remove-Job

$collecting = $false
