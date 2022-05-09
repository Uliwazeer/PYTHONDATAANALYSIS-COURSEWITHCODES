# EX1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


cars = [3, 2, 5, 1]
names = ['Audi', 'BMW', 'Mercedis', 'Ferreri']
plt.pie(
    cars, labels=names, labeldistance=1.1,
    # explode => to cut anything from you circle
    explode=[0, 0, 0, 0], radius=1.1,
    startangle=0, colors=['red', 'blue', 'green', 'yellow'],
    rotatelabels=False, autopct='%1.0f%%'
)
plt.show()
# EX2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


cars = [3, 2, 5, 1]
names = ['Audi', 'BMW', 'Mercedis', 'Ferreri']
plt.pie(
    cars, labels=names, labeldistance=1.1,
    # explode => to cut anything from you circle
    explode=[.2, 0.1, 0.1, 0], radius=1.1,
    startangle=0, colors=['red', 'blue', 'green', 'yellow'],
    rotatelabels=False, autopct='%1.0f%%' #autopct=>auto percentage
)
plt.show()
