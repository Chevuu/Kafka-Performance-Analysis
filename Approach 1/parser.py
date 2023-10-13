import sys
import re

def parse_cpu_values(filename):
    cpu_values = []
    kafka_lines = 0
    with open(filename, 'r', encoding='latin-1') as file:
        for line in file:
            match = re.search(r'Kafka\s+([\d.]+)%', line)
            if match:
                cpu_values.append(float(match.group(1)))
            if line.startswith("Kafka"):
                kafka_lines += 1

    return cpu_values, kafka_lines

def calculate_mean(values):
    if not values:
        return None
    return sum(values) / len(values)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Parse CPU values and count Kafka lines from the file
    cpu_values, kafka_lines = parse_cpu_values(file_path)

    # Calculate mean of CPU values
    mean_cpu = calculate_mean(cpu_values)

    # Print the mean CPU value and the number of Kafka lines
    if mean_cpu is not None:
        print(f"Mean CPU value: {mean_cpu:.2f}")
    else:
        print("No CPU values found.")
    print(f"Number of Kafka lines: {kafka_lines}")
