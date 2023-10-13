import matplotlib.pyplot as plt

# Data from the provided example
num_producers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#cpu_percent = []
mem_size = [598.24, 642.05, 686.09, 723.48, 747.71, 785.54, 820.91, 835.78, 925.16, 936.45]

# Plotting CPU percent for different numbers of producers
fig, ax1 = plt.subplots()

# Plot CPU percent
ax1.bar(num_producers, mem_size, color='skyblue', label='Mem Size')
ax1.set_xlabel('Number of Producers')
ax1.set_ylabel('Mem Size (in MiB)', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('Mem size Usage for Different Number of Producers')
plt.show()
