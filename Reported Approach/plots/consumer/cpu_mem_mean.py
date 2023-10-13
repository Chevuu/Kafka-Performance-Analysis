def read_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        # Skip the first line
        next(file)
        line_count = 0

        for line in file:
            line_count += 1

            # Skip every second line
            if line_count % 2 == 0:
                continue

            parts = line.strip().split()
            if len(parts) == 4:
                container = parts[0]
                cpu_percent = float(parts[1].strip('%'))
                mem_usage = float(parts[3].strip('MiB'))
                data.append({"Container": container, "CPU %": cpu_percent, "MEM USAGE": mem_usage})

    return data


def calculate_mean(data):
    total_cpu = 0.0
    total_mem = 0.0
    count = len(data)

    for record in data:
        total_cpu += record["CPU %"]
        total_mem += record["MEM USAGE"]

    mean_cpu = total_cpu / count if count > 0 else 0.0
    mean_mem = total_mem / count if count > 0 else 0.0

    return mean_cpu, mean_mem


filename = "docker_stats_Kafka_Cons0.txt"
data = read_data_from_file(filename)

mean_cpu, mean_mem = calculate_mean(data)

print("Mean CPU Percent:", mean_cpu)
print("Mean Memory Usage (in MiB):", mean_mem)
