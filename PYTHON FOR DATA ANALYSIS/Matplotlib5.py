# EX1
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn")
area = np.array([100, 200, 300, 400, 500, 600])
price = np.array([1000, 2000, 3000, 4000, 5000, 6000])
# Scatter put points on diagram instead diagram of linear
plt.scatter(area, price, marker='o', c="red", s=50)
plt.show()
# EX2
plt.style.use("seaborn")
area = np.array([100, 200, 300, 400, 500, 600])
price = np.array([1000, 2000, 3000, 4000, 5000, 6000])
# Scatter put points on diagram instead diagram of linear
# we can use this styles in marker['o','.','x','v','d','s',]
plt.scatter(area, price, marker='Uli', c="blue", s=60)  # c=color ,s=size
plt.show()
# EX3
plt.style.use("seaborn")
area = np.random(200)
price = np.random(150 )
# Scatter put points on diagram instead diagram of linear
# we can use this styles in marker['o','.','x','v','d','s',]
plt.scatter(area, price, marker='Uli', c="blue", s=60)  # c=color ,s=size
plt.show()
