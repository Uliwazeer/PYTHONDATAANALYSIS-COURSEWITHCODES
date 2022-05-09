# https://pandas.pydata.org/docs/search.html?q=series=>(resource)
# ex1
import pandas as pd
import pandas as pd 
ls = ["ALI","ULI","ALY","ULY","NOOR","NOUR","3LI","ALI"]
ser = pd.Series(ls)
print("\n")
print(ls)
print("\n")
print(ser)
print("\n")
print("\n")
# ex2
import pandas as pd 
ls = [12,1,3,52,8,5,9,2,5,2,5,2,5,5,6,2,5,5]
ser = pd.Series(ls)
print("\n")
print(ls)
print("\n")
print(ser)
print("\n")
print("\n")
# ex3
ls = ["ALI", "ULI", "ALY", "ULY", "NOOR", "NOUR", "3LI", "ALI"]
ser = pd.Series(ls.index['a','b','c','d','e','f','g','h'])
print("\n")
print(ls)
print("\n")
print(ser)
print("\n")
print("\n")
# ex4
ls = ["ALI", "ULI", "ALY", "ULY", "NOOR", "NOUR", "3LI", "ALI"]
ser = pd.Series(ls.index['a','b','c','d','e','f','g','h'])
print("\n")
print(ls.values)
print(ls.index)
print("\n")
print(ser)
print(ser.values)
print(ser.index)
print("\n")
print("\n")
# PANDAS LIBRARY
# Examples

# Constructing Series from a dictionary with an Index specified

# d = {'a': 1, 'b': 2, 'c': 3}
# ser = pd.Series(data=d, index=['a', 'b', 'c'])
# ser
# a   1
# b   2
# c   3
# dtype: int64
# The keys of the dictionary match with the Index values, hence the Index values have no effect.

# d = {'a': 1, 'b': 2, 'c': 3}
# ser = pd.Series(data=d, index=['x', 'y', 'z'])
# ser
# x   NaN
# y   NaN
# z   NaN
# dtype: float64
# Note that the Index is first build with the keys from the dictionary. After this the Series is reindexed with the given Index values, hence we get all NaN as a result.

# Constructing Series from a list with copy = False.

# r = [1, 2]
# ser = pd.Series(r, copy=False)
# ser.iloc[0] = 999
# r
# [1, 2]
# ser
# 0    999
# 1      2
# dtype: int64
# Due to input data type the Series has a copy of the original data even though copy = False, so the data is unchanged.

# Constructing Series from a 1d ndarray with copy = False.

# r = np.array([1, 2])
# ser = pd.Series(r, copy=False)
# ser.iloc[0] = 999
# r
# array([999,   2])
# ser
# 0    999
# 1      2
# dtype: int64
