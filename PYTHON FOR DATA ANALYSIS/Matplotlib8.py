# EX1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')
# data for a three dimensional line
x = np.array([100, 200, 300, 400, 500])
y = np.array([1100, 1200, 1300, 1400, 1500])
z = np.array([1, 2, 3, 4, 5])

# data for three dimensional scattered points
ax.scatter3D(x, y, z, c='black')
plt.show()


# EX2

ax = plt.axes(projection='3d')
# data for a three dimensional line
x = np.array([100, 200, 300, 400, 500])
y = np.array([1100, 1200, 1300, 1400, 1500])
z = np.array([1, 2, 3, 4, 5])
ax.plot3D(x, y, z, "red")

# data for three dimensional scattered points
# ax.scatter3D(x,y,z,c='black')
plt.show()
