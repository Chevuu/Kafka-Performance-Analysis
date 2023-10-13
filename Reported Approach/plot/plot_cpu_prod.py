import matplotlib.pyplot as plt

# Data from the provided example
num_producers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cpu_percent = [135.56, 272.25, 421.56, 549.73, 651.46, 679.76,  717.58, 710.12, 727.52, 751.30]
# nb_messages = [88, 94, 108, 138, 193, 201, 205, 219, 229, 238]

# Plotting CPU percent for different numbers of consumers
fig, ax1 = plt.subplots()

# Plot CPU percent
ax1.bar(num_producers, cpu_percent, color='skyblue', label='CPU %')
ax1.set_xlabel('Number of Producers')
ax1.set_ylabel('CPU %', color='skyblue')
ax1.tick_params('y', colors='skyblue')

plt.title('CPU Usage for Different Number of Producers')
plt.show()
