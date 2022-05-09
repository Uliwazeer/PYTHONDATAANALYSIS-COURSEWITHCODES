# ex1
from hashlib import new
from multiprocessing import managers
import pandas as pd 
worker = [
    ["Ali","Engineer"],
    ["Noor","Farmar"],
    ["Anwar","Assestant"],
    ["Aliaaa","Driver"],
    ["Aly","Accountant"],
    ["Alia","Teacher"],
    ["Alaa","HR"],
]


managers = [
    ["Omar","Accountant"],
    ["Tarek","Engineer"],
    [None,"HR"]
]

worker_df = pd.DataFrame(worker,columns=['Name','Section'])
mangers_df = pd.DataFrame(managers,columns=['Manger','Section'])

print(worker_df)
print("\n")
print(mangers_df)
print("\n")
new_table = pd.merge(worker_df,mangers_df)
print(new_table)