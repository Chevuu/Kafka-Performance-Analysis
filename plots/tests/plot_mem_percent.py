import matplotlib.pyplot as plt

# Data from the provided example
num_consumers = [0, 1, 2, 3, 4, 5]
mem_percent = [6.87, 6.85, 8.95, 8.95, 11.52, 13.13]

# Plotting memory percent for different numbers of consumers
plt.bar(num_consumers, mem_percent, color='lightgreen')
plt.xlabel('Number of Consumers')
plt.ylabel('Memory %')
plt.title('Memory Usage for Different Numbers of Consumers')
plt.show()
