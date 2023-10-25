import sys

# Define column descriptions for the new format
column_descriptions = {
    0: "User CPU Usage (%)",
    1: "System CPU Usage (%)",
    2: "Idle CPU (%)",
    3: "Wait CPU (%)",
    4: "Stolen CPU (%)",
    5: "Used Memory (MB)",
    6: "Free Memory (MB)",
    7: "Buffer Memory (MB)",
    8: "Cache Memory (MB)"
}

# Check if a file argument is provided
if len(sys.argv) != 2:
    print("Usage: python parse_dstat.py <dstat_data_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Initialize dictionaries to store column totals and counts
column_totals = {}
column_counts = {}
linenum = 0

# Open and read the dstat data file
with open(input_file, 'r') as file:
    for line in file:
        if not (line.startswith('--') or line.startswith('usr')):
            # Replace '|' with space and split the line into columns
            line = line.replace('|', ' ')
            columns = line.strip().split()

            # Ignore lines with fewer columns
            if len(columns) != 9:  # Update the number of columns
                print(f"Ignoring line {linenum}: {len(columns)} columns found")
                continue

            # Extract and parse the numerical values
            values = columns[0:9]  # Update the number of columns
            for i, value in enumerate(values):
                # Initialize column totals and counts
                if i not in column_totals:
                    column_totals[i] = 0.0
                    column_counts[i] = 0

                try:
                    # Remove 'M' if present and convert to float
                    value = float(value.replace('M', ''))
                    # Add the value to the total and increment the count
                    column_totals[i] += value
                    column_counts[i] += 1
                except ValueError:
                    pass

        linenum += 1

# Calculate and print the averages with descriptions
for column, total in column_totals.items():
    if column_counts[column] > 0:
        avg = total / column_counts[column]
        description = column_descriptions.get(column, "Unknown")
        print(f"Average for {description}: {avg:.2f} MB")
    else:
        description = column_descriptions.get(column, "Unknown")
        print(f"No data for {description}")
