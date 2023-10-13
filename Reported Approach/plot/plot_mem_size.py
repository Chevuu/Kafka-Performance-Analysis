import matplotlib.pyplot as plt

# Data from the provided example
size = ["2^2", "2^8", "2^10", "2^12", "2^15", "2^20", "2^25"]
# cpu_percent = [135.65, 133.61, 135.94, 134.91, 137.40, 186.96, 301.50]
mem_size = [650.32, 646.03, 648.86, 718.85, 763.09, 1514.42, 1882.95]
# nb_messages = [112, 106, 124, 116, 112, 149, 151, 148, 145, 159]

# Plotting CPU percent for different numbers of consumers
fig, ax1 = plt.subplots()

# Plot CPU percent
ax1.bar(size, mem_size, color='skyblue', label='Mem Size')
ax1.set_xlabel('Number of Consumers')
ax1.set_ylabel('Mem Size (in MiB)', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('Mem size Usage for Different Number of Consumers')
plt.show()
