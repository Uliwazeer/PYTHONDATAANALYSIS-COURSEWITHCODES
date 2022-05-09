# EX1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("datafile.csv")
print(data)


# corretion => measure what elements have a relation with anthor elements or no
c = data.corr()
print(c)
# heatmap()=>as digram explain values using a plot
sns.heatmap(corr, annot=true)  # annotation
sns.pairplot(data)
plt.show()
