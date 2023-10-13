import matplotlib.pyplot as plt

# Data from the provided example
num_consumers = [0, 1, 2, 3, 4, 5]
cpu_percent = [112.840576923077,111.305576923077,113.144423076923,113.973773584906,105.961730769231,105.530961538462
]
mem_percent = [6.41219916595488,8.62560920464251,9.99766366879365,11.3886348791639,12.5904888710245,13.5379088579611]

# Plotting the data
plt.bar(num_consumers, cpu_percent, label='CPU %')
plt.bar(num_consumers, mem_percent, label='MEM %', alpha=0.5)

plt.xlabel('Number of Consumers')
plt.ylabel('Percentage')
plt.title('CPU and Memory Usage for Different Numbers of Consumers')
plt.legend()

plt.show()
