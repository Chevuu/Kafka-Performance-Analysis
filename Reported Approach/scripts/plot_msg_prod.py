import matplotlib.pyplot as plt

num_producers = [1, 2, 3, 4, 5, 6, 7, 8]
num_messages = [17, 28, 44, 50, 53, 55, 57, 58]

fig, ax1 = plt.subplots()

ax1.bar(num_producers, num_messages, color='skyblue', label='CPU %')
ax1.set_xlabel('Number of Producers')
ax1.set_ylabel('Number of messages successfully delivered', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('Throughput Measuring')
plt.show()