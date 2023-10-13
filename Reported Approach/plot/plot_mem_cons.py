import matplotlib.pyplot as plt

num_consumers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mem_size = [1324.73, 1427.71, 1518.29, 1611.63, 1736.16, 1873.14, 1968.62, 2046.84, 1982.80, 2124.06]

fig, ax1 = plt.subplots()

ax1.bar(num_consumers, mem_size, color='skyblue', label='Mem Size')
ax1.set_xlabel('Number of Consumers')
ax1.set_ylabel('Mem Size (in MiB)', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('Mem size Usage for Different Number of Consumers')
plt.show()
