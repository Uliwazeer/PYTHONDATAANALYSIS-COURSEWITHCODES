# EX1
from cProfile import label
import pandas as pd
import numpy as np
from sklearn import preprocessing
data = pd.read_csv("datafile.csv", header=0)
print(data)

le = preprocessing.LabelEncoder()
labeling = le.fit_transform(data["country"])
print("\n")
print(labeling)
data["country"] = labeling
print(data)
print("\n")
print(le.classes)
