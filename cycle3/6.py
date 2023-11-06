import matplotlib.pyplot as plt
# Height data
heights = [61, 63, 64, 66, 68, 69, 71, 71.5, 72, 72.5, 73, 73.5, 74, 74.5, 76, 76.2, 76.5, 77, 77.5, 78, 78.5, 79, 79.2, 80, 81, 82, 83, 84, 85, 87]
# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(heights, bins=range(60, 90, 5), edgecolor='black', alpha=0.7)
# Set labels and title
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')
plt.title('Cherry Tree Heights Histogram')
# Add grid
plt.grid(True)
# Show the histogram
plt.show()
