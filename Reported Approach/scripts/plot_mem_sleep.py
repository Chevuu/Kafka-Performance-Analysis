import matplotlib.pyplot as plt

sleep_time = [0.01, 0.05, 0.125, 0.25, 0.5, 1, 2, 4]
mem_size = [648.50, 654.46, 651.19, 648.96, 642.63, 639.42, 628.43, 623.22]

fig, ax1 = plt.subplots()

ax1.bar(range(len(sleep_time)), mem_size, color='skyblue', label='Mem Size')
ax1.set_xticks(range(len(sleep_time)))
ax1.set_xticklabels([str(t) for t in sleep_time])
ax1.set_xlabel('Frequency of sending messages (in seconds)')
ax1.set_ylabel('Mem Size (in MiB)', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('Mem size Usage for Different Frequency of sending messages')
plt.show()
