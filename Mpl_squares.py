#encoding=utf8
import matplotlib.pyplot as plt
x_value=[i for i in range(1000)]
squares=[i**2 for i in range(1000)]

plt.plot(x_value,squares,linewidth=2)

plt.title("square",fontsize=20)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()