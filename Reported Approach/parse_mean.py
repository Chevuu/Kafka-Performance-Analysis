import sys
import re

def parse_cpu_mem_values(filename):
    cpu_values = []
    mem_values = []
    kafka_lines = 0
    with open(filename, 'r', encoding='latin-1') as file:
        for line in file:
            match = re.search(r'Kafka\s+(\d+\.\d+)%.*?(\d+\.\d+)([MGT])iB.*?(\d+\.\d+)([MGT])iB', line)
            if match:
                cpu_percentage = float(match.group(1))
                mem_usage = float(match.group(2))
                mem_usage_unit = match.group(3)
                mem_limit = float(match.group(4))
                mem_limit_unit = match.group(5)

                # Convert MEM usage and limit to MiB
                if mem_usage_unit == 'G':
                    mem_usage *= 1024  # Convert GiB to MiB
                if mem_limit_unit == 'G':
                    mem_limit *= 1024  # Convert GiB to MiB

                cpu_values.append(cpu_percentage)
                mem_values.append(mem_usage)

            if line.startswith("Kafka"):
                kafka_lines += 1

    return cpu_values, mem_values, kafka_lines

def calculate_mean(values):
    if not values:
        return None
    return sum(values) / len(values)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Parse CPU and MEM values, and count Kafka lines from the file
    cpu_values, mem_values, kafka_lines = parse_cpu_mem_values(file_path)

    # Calculate the mean of CPU and MEM values
    mean_cpu = calculate_mean(cpu_values)
    mean_mem = calculate_mean(mem_values)

    # Print the mean CPU and MEM values, and the number of Kafka lines
    if mean_cpu is not None:
        print(f"Mean CPU value: {mean_cpu:.2f}%")
    else:
        print("No CPU values found.")
    
    if mean_mem is not None:
        print(f"Mean MEM value: {mean_mem:.2f} MiB")
    else:
        print("No MEM values found.")

    print(f"Number of Kafka lines: {kafka_lines}")
