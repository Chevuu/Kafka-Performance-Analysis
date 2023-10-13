import matplotlib.pyplot as plt

size = ["2^2", "2^8", "2^10", "2^12", "2^15", "2^20", "2^25"]
mem_size = [650.32, 646.03, 648.86, 718.85, 763.09, 1514.42, 1882.95]

fig, ax1 = plt.subplots()

ax1.bar(size, mem_size, color='skyblue', label='Mem Size')
ax1.set_xlabel('Number of Consumers')
ax1.set_ylabel('Mem Size (in MiB)', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('Mem size Usage for Different Message Size')
plt.show()
