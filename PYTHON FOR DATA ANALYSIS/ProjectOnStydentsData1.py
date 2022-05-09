# EX1
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from re import A
import pandas as pd
import numpy as np
data = pd.read_csv("datafile.csv")
print(data.columns)
print(data.isnull().sum())
# EX2
data = pd.read_csv("datafile.csv")
data = data.drop(["test preparation course", "race/ethnicity"], axis=1)
print(data)
print(data.isnull().sum())
# EX3
data = pd.read_csv("datafile.csv")
# data cleaning
data = data.drop(["test preparation course", "race/ethnicity"], axis=1)
# lebaling
object_data = data.select_dtypes(include=["object"])
print(object_data)
le = preprocessing.LabelEncoder()
c = data.corr()
print(c)
sns.heatmap(c, annot=true)
plt.show()
# EX4 Using For Loop to Store Data In Every Raws
data = pd.read_csv("datafile.csv")
# data cleaning
data = data.drop(["test preparation course", "race/ethnicity"], axis=1)
# lebaling
object_data = data.select_dtypes(include=["object"])
print(object_data)
le = preprocessing.LabelEncoder()
for i in range(object_data.shape[1]):
    object_data.iloc[:, i] = le.fit_transform(object_data.iloc[:, i])
# concate
num_data = data.select_dtypes(exclude=["object"])
data = pd.concat([object_data, num_data], axis=1)
# relationship
c = data.corr()
print(c)
sns.heatmap(c, annot=true)
plt.show()
