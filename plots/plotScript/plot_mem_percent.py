import matplotlib.pyplot as plt

# Data from the provided example
num_consumers = [0, 1, 2, 3, 4, 5]
mem_percent = [6.41219916595488,8.62560920464251,9.99766366879365,11.3886348791639,12.5904888710245,13.5379088579611]

# Plotting memory percent for different numbers of consumers
plt.bar(num_consumers, mem_percent, color='lightgreen')
plt.xlabel('Number of Consumers')
plt.ylabel('Memory %')
plt.title('Memory Usage for Different Numbers of Consumers')
plt.show()
