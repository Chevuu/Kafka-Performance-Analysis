import matplotlib.pyplot as plt

# Data from the provided example
num_consumers = [0, 1, 2, 3, 4, 5]
cpu_percent = [1.45, 101.35, 174.48, 145.05, 174.83, 174.47]
mem_percent = [6.87, 6.85, 8.95, 8.95, 11.52, 13.13]

# Plotting the data
plt.bar(num_consumers, cpu_percent, label='CPU %')
plt.bar(num_consumers, mem_percent, label='MEM %', alpha=0.5)

plt.xlabel('Number of Consumers')
plt.ylabel('Percentage')
plt.title('CPU and Memory Usage for Different Numbers of Consumers')
plt.legend()

plt.show()
