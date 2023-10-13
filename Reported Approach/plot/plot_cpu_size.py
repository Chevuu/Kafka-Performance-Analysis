import matplotlib.pyplot as plt
import numpy as np

size = ["2^2", "2^8", "2^10", "2^12", "2^15", "2^20", "2^25"]
cpu_percent = [135.65, 133.61, 135.94, 134.91, 137.40, 186.96, 301.50]
# nb_messages = [90, 88, 88, 88, 92, 106, 649]

# Increase the bar width
bar_width = 0.5

# Custom x-axis positions and labels
x_positions = np.arange(len(size))  # Positions for each 'size' value
x_labels = [str(s) for s in size]  # Labels for 'size' values

# Plotting CPU percent for different numbers of consumers
fig, ax1 = plt.subplots()

# Plot CPU percent with increased bar width
ax1.bar(x_positions, cpu_percent, width=bar_width, color='skyblue', label='CPU %')
ax1.set_xlabel('Message Size (in bits)')
ax1.set_ylabel('CPU %', color='skyblue')
ax1.set_xticks(x_positions)  # Set the custom x-axis positions
ax1.set_xticklabels(x_labels)  # Set the custom x-axis labels
ax1.tick_params('y', colors='skyblue')

# Creating a second y-axis to plot nb_messages
# ax2 = ax1.twinx()
# ax2.plot(x_positions, nb_messages, color='red', marker='o', label='Number of Messages')
# ax2.set_ylabel('Number of Messages', color='red')
# ax2.tick_params('y', colors='red')

plt.title('CPU Usage for Different Message Size')
plt.show()
