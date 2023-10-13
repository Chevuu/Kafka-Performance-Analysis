import matplotlib.pyplot as plt

# Data from the provided example
num_consumers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#cpu_percent = [118.82, 115.78, 129.33, 125.22, 122.60, 144.61, 138.64, 140.30, 147.95, 152.79]
mem_size = [1324.73, 1427.71, 1518.29, 1611.63, 1736.16, 1873.14, 1968.62, 2046.84, 1982.80, 2124.06]
# nb_messages = [112, 106, 124, 116, 112, 149, 151, 148, 145, 159]

# Plotting CPU percent for different numbers of consumers
fig, ax1 = plt.subplots()

# Plot CPU percent
ax1.bar(num_consumers, mem_size, color='skyblue', label='Mem Size')
ax1.set_xlabel('Number of Consumers')
ax1.set_ylabel('Mem Size (in MiB)', color='skyblue')
ax1.tick_params('y', colors='skyblue')

# Creating a second y-axis to plot nb_messages
# ax2 = ax1.twinx()
# ax2.plot(num_consumers, nb_messages, color='red', marker='o', label='Number of Messages')
# ax2.set_ylabel('Number of Messages', color='red')
# ax2.tick_params('y', colors='red')

plt.title('Mem size Usage for Different Number of Consumers')
plt.show()
