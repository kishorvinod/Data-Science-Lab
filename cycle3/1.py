import matplotlib.pyplot as plt


years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]


fig, ax = plt.subplots()


ax.plot(years, car_values, color='red', linestyle='-.', marker='*', markersize=20, markerfacecolor='green')


ax.set_xlabel('Year')
ax.set_ylabel('Car Value')
ax.set_title('Value Depreciation', loc='left')


plt.show()
