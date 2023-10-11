def calculate_mean(data):
    total_cpu = 0.0
    total_mem = 0.0
    count = 0

    for record in data:
        cpu_percent_str = record["CPU %"]
        mem_usage_str = record["MEM USAGE / LIMIT"]

        # Skip empty or non-convertible values
        if cpu_percent_str == '' or mem_usage_str == '':
            continue

        cpu_percent = float(cpu_percent_str[:-1])  # remove the '%' sign and convert to float
        mem_usage = float(mem_usage_str.split('/')[0].strip()[:-1])  # extract memory usage and convert to float

        total_cpu += cpu_percent
        total_mem += mem_usage
        count += 1

    mean_cpu = total_cpu / count if count > 0 else 0.0
    mean_mem = total_mem / count if count > 0 else 0.0

    return mean_cpu, mean_mem



def read_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[2:]:  # Skip the header lines
            parts = line.strip().split()
            if len(parts) >= 3:
                cpu_percent, mem_usage = parts[1], parts[2]
                data.append({"CPU %": cpu_percent, "MEM USAGE / LIMIT": mem_usage})

    return data



filename = "docker_stats_Kafka_Cons0.txt"
data = read_data_from_file(filename)

mean_cpu, mean_mem = calculate_mean(data)

print("Mean CPU Percent:", mean_cpu)
print("Mean Memory Percent:", mean_mem)

