import matplotlib.pyplot as plt

# Data from the provided example
sleep_time = [0.01, 0.05, 0.125, 0.25, 0.5, 1, 2, 4]
cpu_percent = [153.33, 149.15, 145.22, 131.32, 114.91, 90.69, 63.28, 40.97]
# nb_messages = [78, 80, 84, 90, 106, 136, 192, 309]

# Plotting CPU percent for different numbers of consumers
fig, ax1 = plt.subplots()

# Plot CPU percent
ax1.bar(range(len(sleep_time)), cpu_percent, color='skyblue', label='CPU %')
ax1.set_xticks(range(len(sleep_time)))
ax1.set_xticklabels([str(t) for t in sleep_time])
ax1.set_xlabel('Frequency of sending messages (in seconds)')
ax1.set_ylabel('CPU %', color='skyblue')
ax1.tick_params('y', colors='skyblue')

# Creating a second y-axis to plot nb_messages
# ax2 = ax1.twinx()
# ax2.plot(sleep_time, nb_messages, color='red', marker='o', label='Number of Messages')
# ax2.set_ylabel('Number of Messages', color='red')
# ax2.tick_params('y', colors='red')

plt.title('CPU Usage for Different Frequency of sending messages')
plt.show()
