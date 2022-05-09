# THE RESOURCES=>
#EX1
import matplotlib.pyplot as plt 
x = [100,200,300,400,500]
y = [1000,2000,3000,4000,5000]
plt.plot(x,y)
plt.show()
#EX2
import matplotlib.pyplot as plt 
x = [2100,2200,2300,2400,2500]
y = [1000,2000,3000,4000,5000]
plt.plot(x,y)
plt.show()
#EX3 when you want to change the color
import matplotlib.pyplot as plt 
x = [2100,2200,2300,2400,2500]
y = [1000,2000,3000,4000,5000]
plt.plot(x,y,color="r") #or plt.plot(x,y,color="red")
#plt.plot(x, y, color="#FFF")
plt.show()
#EX4 when you want to change the Size of line in chart linewidth=2px by default
import matplotlib.pyplot as plt 
x = [2100,2200,2300,2400,2500]
y = [1000,2000,3000,4000,5000]
plt.plot(x,y,color="r",linewidth=12)
plt.show()