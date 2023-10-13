import matplotlib.pyplot as plt

sleep_time = [0.01, 0.05, 0.125, 0.25, 0.5, 1, 2, 4]
cpu_percent = [153.33, 149.15, 145.22, 131.32, 114.91, 90.69, 63.28, 40.97]

fig, ax1 = plt.subplots()

ax1.bar(range(len(sleep_time)), cpu_percent, color='skyblue', label='CPU %')
ax1.set_xticks(range(len(sleep_time)))
ax1.set_xticklabels([str(t) for t in sleep_time])
ax1.set_xlabel('Frequency of sending messages (in seconds)')
ax1.set_ylabel('CPU %', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('CPU Usage for Different Frequency of sending messages')
plt.show()
