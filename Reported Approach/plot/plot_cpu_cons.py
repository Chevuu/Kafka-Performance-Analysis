import matplotlib.pyplot as plt

num_consumers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cpu_percent = [118.82, 115.78, 129.33, 125.22, 122.60, 144.61, 138.64, 140.30, 147.95, 152.79]

fig, ax1 = plt.subplots()

ax1.bar(num_consumers, cpu_percent, color='skyblue', label='CPU %')
ax1.set_xlabel('Number of Consumers')
ax1.set_ylabel('CPU %', color='skyblue')
ax1.tick_params('y', colors='skyblue')


plt.title('CPU Usage for Different Number of Consumers')
plt.show()
