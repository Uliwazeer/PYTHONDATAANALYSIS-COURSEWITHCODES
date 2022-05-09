# EX1
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("datafile.csv", header=0)
data = data.drop(["data"], axis=1)
data = data.select_dtypes(exclude=["object"])
c = data.corr()
sns.heatmap(c, annot=true)
plt.scatter(data["sqft_living"], data["bedrooms"])
plt.show()
print(data)
