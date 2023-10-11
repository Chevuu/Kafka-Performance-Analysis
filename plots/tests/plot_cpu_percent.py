import matplotlib.pyplot as plt

# Data from the provided example
num_consumers = [0, 1, 2, 3, 4, 5]
cpu_percent = [1.45, 101.35, 174.48, 145.05, 174.83, 174.47]

# Plotting CPU percent for different numbers of consumers
plt.bar(num_consumers, cpu_percent, color='skyblue')
plt.xlabel('Number of Consumers')
plt.ylabel('CPU %')
plt.title('CPU Usage for Different Numbers of Consumers')
plt.show()
