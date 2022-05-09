# DATA FRAME
# https://pandas.pydata.org/docs/search.html?q=series=>(resourse)
# ex1
import pandas as pd
ls = [1000, 2000, 3000, 4000, 5000]
ser = pd.Series(ls)
print("\n")
print(ser)
print("\n")
print(ls)
print("\n")
print(ser.describe())
# ex2
ls = ["ALI", "SSS", "EEE", "TTT", "UUU", "UIP", "HYTRE", "VXBXB"]
ser = pd.Series(ls)
print("\n")
print(ser)
print("\n")
print(ls)
print("\n")
print(ser.describe())
# ex3
ls = ["ALI", "SSS", "EEE", "TTT", "UUU", "UIP", "HYTRE", "VXBXB"]
ser = pd.Series(ls)
print("\n")
print(ser)
print("\n")
print(ls)
print("\n")
print(ser.mean())
print(ser.std())
print(ser.count())
print(ser.min())
print(ser.sum())
# ex4
ls = ["ALI", "SSS", "EEE", "TTT", "UUU", "UIP", "HYTRE", "VXBXB"]
ser = pd.Series(ls)
print("\n")
print(ser)
print("\n")
print(ls)
print("\n")
# aggiaton(to collect every data to print)
print(ser.agg(['min', 'count', 'std', 'sum']))
