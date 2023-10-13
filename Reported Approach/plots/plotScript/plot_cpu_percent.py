import matplotlib.pyplot as plt

# Data from the provided example
num_consumers = [0, 1, 2, 3, 4, 5]
cpu_percent = [112.840576923077,111.305576923077,113.144423076923,113.973773584906,105.961730769231,105.530961538462
]

# Plotting CPU percent for different numbers of consumers
plt.bar(num_consumers, cpu_percent, color='skyblue')
plt.xlabel('Number of Consumers')
plt.ylabel('CPU %')
plt.title('CPU Usage for Different Numbers of Consumers')
plt.show()
