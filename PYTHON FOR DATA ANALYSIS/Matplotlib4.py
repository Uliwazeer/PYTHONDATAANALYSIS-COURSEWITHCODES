# EX1
from turtle import title
import numpy as np
import matplotlib.pyplot as plt
x = [2100, 2200, 2300, 2400, 2500]
y = [1000, 2000, 3000, 4000, 5000]
z = [440, 880, 990, 770, 883]
# subplot(rows,column,num) function drawing two diagram with inside 
plt.subplot(2,1,1)
plt.plot(x,y)
plt.subplot(2,1,2)
plt.plot(x,z)
plt.show()
# EX2
import numpy as np
import matplotlib.pyplot as plt
x = [2100, 2200, 2300, 2400, 2500]
y = [1000, 2000, 3000, 4000, 5000]
z = [440, 880, 990, 770, 883]
a = plt.axes()
a.set(title="Graph",xlabel='X',ylabel='Y')
plt.plot(x,y)
plt.show()
plt.plot(x,z)
plt.show()
