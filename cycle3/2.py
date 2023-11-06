import matplotlib.pyplot as plt

days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
drinks_sales = [300, 450, 150, 400, 650]
food_sales = [400, 500, 350, 300, 500]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

ax1.plot(days, drinks_sales, linestyle='--', color='cyan')
ax1.scatter(days, drinks_sales, marker='H', color='magenta', edgecolors='black')

ax1.set_xlabel('Days of the Week')
ax1.set_ylabel('Sale of Drinks')
ax1.set_title('Sales Data1', loc='right')

ax1.grid(color='blue', linestyle='--')

ax2.plot(days, food_sales, linestyle='-', color='yellow')
ax2.scatter(days, food_sales, marker='D', color='green', edgecolors='red')

ax2.set_xlabel('Days of the Week')
ax2.set_ylabel('Sale of Food')
ax2.set_title('Sales Data2', loc='center')

ax2.grid(color='blue', linestyle='--')

plt.tight_layout()
plt.show()
