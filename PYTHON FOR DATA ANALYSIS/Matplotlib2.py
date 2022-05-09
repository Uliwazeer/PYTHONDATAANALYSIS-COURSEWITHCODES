# EX1 MATPLOTLIB STYLE SHEET SEARCH ON GOOGLE
import matplotlib.pyplot as plt
# style =>meaning of class of color.
# we use every style on itself
# style=>1
plt.style.use("classic")
# style=>2
plt.style.use("bmh")
# style=>3
plt.style.use("seaborn")
# style=>4
plt.style.use("seaborn-whitegrid")
# style=>5
plt.style.use("seaborn-paper")
# style=>6
plt.style.use("dark_background")
x = [2100, 2200, 2300, 2400, 2500]
y = [1000, 2000, 3000, 4000, 5000]
plt.plot(x, y, color="r", linewidth=12)
plt.show()
# EX2
# style =>meaning of class of color.
# we use every style on itself
# style=>1
plt.style.use("classic")
# style=>2
plt.style.use("bmh")
# style=>3
plt.style.use("seaborn")
# style=>4
plt.style.use("seaborn-whitegrid")
# style=>5
plt.style.use("seaborn-paper")
# style=>6
plt.style.use("dark_background")
x = [2100, 2200, 2300, 2400, 2500]
y = [1000, 2000, 3000, 4000, 5000]
# there are 4 of type linestyle=>(solid,dotted,dashed,dashdot)
# there anther way to write linestyle using sympole
plt.plot(x, y, color="r", linewidth=12, linestyle='solid')  # linestyle='-'
plt.plot(x, y, color="r", linewidth=12, linestyle='dashdot')  # linestyle='-.'
plt.plot(x, y, color="r", linewidth=12, linestyle='dashed')  # linestyle='--'
plt.plot(x, y, color="r", linewidth=12, linestyle='dotted')  # linestyle=':'
plt.show()
# EX3
# style =>meaning of class of color.
# we use every style on itself
# style=>1
plt.style.use("classic")
# style=>2
plt.style.use("bmh")
# style=>3
plt.style.use("seaborn")
# style=>4
plt.style.use("seaborn-whitegrid")
# style=>5
plt.style.use("seaborn-paper")
# style=>6
plt.style.use("dark_background")
x = [2100, 2200, 2300, 2400, 2500]
y = [1000, 2000, 3000, 4000, 5000]
# we can add anthor plot to diagram
z = [440, 550, 660, 770, 880]
plt.plot(x, y, x, z color="r", linewidth=12, linestyle='dotted')  # linestyle=':'
plt.show()
# EX4
# style =>meaning of class of color.
# we use every style on itself
# style=>1
plt.style.use("classic")
# style=>2
plt.style.use("bmh")
# style=>3
plt.style.use("seaborn")
# style=>4
plt.style.use("seaborn-whitegrid")
# style=>5
plt.style.use("seaborn-paper")
# style=>6
plt.style.use("dark_background")
x = [2100, 2200, 2300, 2400, 2500]
y = [1000, 2000, 3000, 4000, 5000]
# we can add anthor plot to diagram
z = [440, 550, 660, 770, 880]
plt.plot(x, y color="r", linewidth=12, linestyle='dotted')  # linestyle=':'
plt.plot(x, z color="b", linewidth=15, linestyle='dashed')  # linestyle='--'
plt.show()
