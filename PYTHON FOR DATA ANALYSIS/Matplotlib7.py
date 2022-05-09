# EX1
from email import header
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["Audi","Kai","BMW"])
y = np.array([3,2,5])
plt.bar(x,y,color='red',alpha=.6)
plt.show()
# EX2
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
data = pd.read_csv('datafile.csv',header=0)
print(data)
x = data['DAY']
y = data['NUM']
plt.style.use("seaborn")
plt.title("Uli")
plt.xlabel("DAY")
plt.ylabel("COUNT")
plt.scatter(x,y,color='blue',marker='X',s=100)
plt.plot(x,y,color='black')
plt.bar(x,y,color='red',edgecolor='black',facecolor='white')
# edgecolor=border style
# facecolor=body or front diagram style

plt.show()