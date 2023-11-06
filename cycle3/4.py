import matplotlib.pyplot as plt

product = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
affordable_segment = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
luxury_segment = [189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161]
super_luxury = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]
plt.plot(product, affordable_segment, 'r--', label='Affordable Segment')
plt.plot(product, luxury_segment, 'g-.', label='Luxury Segment')
plt.plot(product, super_luxury, 'b-', label='Super luxury segment')
plt.xlabel('Months of year')
plt.ylabel('Sales of segments')
plt.title('Sales data')
plt.legend(loc='upper right')
plt.show()
