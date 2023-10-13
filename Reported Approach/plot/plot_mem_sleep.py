import matplotlib.pyplot as plt

# Data from the provided example
sleep_time = [0.01, 0.05, 0.125, 0.25, 0.5, 1, 2, 4]
# cpu_percent = [153.33, 149.15, 145.22, 131.32, 114.91, 90.69, 63.28, 40.97]
mem_size = [648.50, 654.46, 651.19, 648.96, 642.63, 639.42, 628.43, 623.22]

# Plotting CPU percent for different numbers of consumers
fig, ax1 = plt.subplots()

# Plot CPU percent
ax1.bar(range(len(sleep_time)), mem_size, color='skyblue', label='Mem Size')
ax1.set_xticks(range(len(sleep_time)))
ax1.set_xticklabels([str(t) for t in sleep_time])
ax1.set_xlabel('Frequency of sending messages (in seconds)')
ax1.set_ylabel('Mem Size (in MiB)', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('Mem size Usage for Different Frequency of sending messages')
plt.show()
