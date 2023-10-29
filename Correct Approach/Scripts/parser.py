import sys

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

if len(sys.argv) != 2:
    print("Usage: python parse_dstat.py <dstat_data_file>")
    sys.exit(1)

input_file = sys.argv[1]

column_totals = {}
column_counts = {}
linenum = 0

with open(input_file, 'r') as file:
    for line in file:
        if not (line.startswith('--') or line.startswith('usr')):
            line = line.replace('|', ' ')
            columns = line.strip().split()

            if len(columns) != 9: 
                print(f"Ignoring line {linenum}: {len(columns)} columns found")
                continue

            values = columns[0:9]  
            for i, value in enumerate(values):
                if i not in column_totals:
                    column_totals[i] = 0.0
                    column_counts[i] = 0

                try:
                    value = float(value.replace('M', ''))
                    column_totals[i] += value
                    column_counts[i] += 1
                except ValueError:
                    pass

        linenum += 1

for column, total in column_totals.items():
    if column_counts[column] > 0:
        avg = total / column_counts[column]
        description = column_descriptions.get(column, "Unknown")
        print(f"Average for {description}: {avg:.2f} MB")
    else:
        description = column_descriptions.get(column, "Unknown")
        print(f"No data for {description}")
