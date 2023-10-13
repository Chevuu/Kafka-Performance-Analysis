import matplotlib.pyplot as plt
import numpy as np

size = ["2^2", "2^8", "2^10", "2^12", "2^15", "2^20", "2^25"]
cpu_percent = [135.65, 133.61, 135.94, 134.91, 137.40, 186.96, 301.50]

bar_width = 0.5

x_positions = np.arange(len(size))  
x_labels = [str(s) for s in size]  

fig, ax1 = plt.subplots()

ax1.bar(x_positions, cpu_percent, width=bar_width, color='skyblue', label='CPU %')
ax1.set_xlabel('Message Size (in bits)')
ax1.set_ylabel('CPU %', color='skyblue')
ax1.set_xticks(x_positions)  
ax1.set_xticklabels(x_labels)  
ax1.tick_params('y', colors='skyblue')

plt.title('CPU Usage for Different Message Size')
plt.show()
