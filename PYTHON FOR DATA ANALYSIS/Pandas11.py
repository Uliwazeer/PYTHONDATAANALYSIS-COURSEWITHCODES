# GROUPING
# EX1
import pandas as pd
data = [
    ["Engineer", 200000],
    ["Engineer", 300000],
    ["Office Boy", 400000],
    ["Accountant", 500000],
    ["Driver", 600000],
    ["Developer", 700000],
    ["HR", 800000],
]

df = pd.DataFrame(data, columns=['Job', 'Sallary'])
print("\n")
print(df)
print("\n")
g = df.groupby("Job").count()
print(g)
# EX2
data = [
    ["Engineer", 200000],
    ["Engineer", 300000],
    ["Office Boy", 400000],
    ["Accountant", 500000],
    ["Driver", 600000],
    ["Developer", 700000],
    ["HR", 800000],
]

df = pd.DataFrame(data, columns=['Job', 'Sallary'])
print("\n")
print(df)
print("\n")
g = df.groupby("Job").count()
for i in g:
    print(i)
# EX3
data = [
    ["Engineer", 200000],
    ["Engineer", 300000],
    ["Office Boy", 400000],
    ["Accountant", 500000],
    ["Driver", 600000],
    ["Developer", 700000],
    ["HR", 800000],
]

df = pd.DataFrame(data, columns=['Job', 'Sallary'])
print("\n")
print(df)
print("\n")
g = df.groupby("Job").sum()
d = df.groupby("Job").meam()
print(g)
print(d)
