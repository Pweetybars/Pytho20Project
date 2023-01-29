import matplotlib.pyplot as plt

x1 = [2, 1, 9, 2, 7, 1]
y1 = [2, 3, 6, 4, 55, 0]

plt.plot(x1,y1, color='black',linestyle = 'dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12 )

x2 = [1, 2, 3]
y2 = [1, 4, 3]

plt.plot(x2,y2, color='green',linestyle = 'dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12 )

plt.ylim(1,8)
plt.xlim(1,8)

plt.xlabel('x Axis')

plt.ylabel('y Axis')
 
plt.title('DemoGraph-Custom')

plt.show()