# EX1
# EX1
from sklearn.impute import SimpleImputer
import pandas as pd
import seaborn as sns
data = pd.read_csv("datafile.csv")
print(data)
print(data.shape)
# EX2
data = pd.read_csv("datafile.csv")
data = data.dropna()
print(data)
# EX3
data = pd.read_csv("datafile.csv")
data = data.dropna()
print(data)
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
# strategy can take this value ,too =>(mean,medium,most_frequent,constant)
cleared_data = imputer.fit_transform(data)
print(cleared_data)


new_data = pd.DataFrame(cleared_data, columns=data.columns)
print(new_data)
# EX4
data = pd.read_csv("datafile.csv")
data = data.dropna()
print(data)
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
# strategy can take this value ,too =>(mean,medium,most_frequent,constant)
cleared_data = imputer.fit_transform(data)
print(cleared_data)
new_data = data.drop(["ID"], axis=1)
print(new_data)
