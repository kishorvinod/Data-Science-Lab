import matplotlib.pyplot as plt
# Data
transport_modes = ['Walking', 'cycling', 'car', 'Bus', 'train']
frequencies = [29, 15, 35, 18, 3]

# Create a bar graph
plt.bar(transport_modes, frequencies, width=0.1, color='green')

# Set labels and title
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')

# Show the bar graph
plt.show()
