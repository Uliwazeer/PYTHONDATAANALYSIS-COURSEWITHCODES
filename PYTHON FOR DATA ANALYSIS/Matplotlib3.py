# EX1
# how to abreviate linestyle with color style on same code
# EX1 MATPLOTLIB STYLE SHEET SEARCH ON GOOGLE
import numpy as np
from cProfile import label
import matplotlib.pyplot as plt

plt.style.use("dark_background")
x = [2100, 2200, 2300, 2400, 2500]
y = [1000, 2000, 3000, 4000, 5000]
z = [440, 880, 990, 770, 883]
# meaning make style dashed and color red equal to plt.plot(x, y, color="r", linewidth=3,linestyle='dasded')
plt.plot(x, y, linewidth=3, "--r")
plt.plot(x, z, ":b", linewidth=3)
# plt.plot(x, y, color="r", linewidth=12)
plt.plot(x, z, color="blue", linewidth=14)
plt.show()
# EX2 ARRAYS
area = np.array([100, 200, 300, 400, 500])
price = np.array([1000, 2000, 3000, 4000, 5000])
plt.plot(area, price)
plt.show()
# EX3 ARRAYS
area = np.array([100, 200, 300, 400, 500])
price = np.array([1000, 2000, 3000, 4000, 5000])
# when you want to give array name
plt.title("Areas VS Price")
# when you want to give axis(x,y) name
plt.xlabel("Area")
plt.ylabel("Price")
plt.plot(area, price)
plt.show()
# EX4 ARRAYS
area = np.array([100, 200, 300, 400, 500])
price = np.array([1000, 2000, 3000, 4000, 5000])
# when you want to give array name
plt.title("Areas VS Price")
# when you want to give axis(x,y) name
plt.xlabel("Area")
plt.ylabel("Price")
# when you want diagram strat from some number
plt.xlim(50, 600)  # x-axis
plt.ylim(50, 600)  # y-axis
plt.plot(area, price)
plt.show()
# EX5 ARRAYS
area = np.array([100, 200, 300, 400, 500])
price = np.array([1000, 2000, 3000, 4000, 5000])
price2 = np.array([1200, 1300, 1400, 1500, 1600])
# when you want to give label to every diagram
plt.plot(area, price, ':b', label="Uli")
plt.plot(area, price2, '--r', label="Wazeer")
plt.plot(area, price)
plt.legend()
plt.show()
