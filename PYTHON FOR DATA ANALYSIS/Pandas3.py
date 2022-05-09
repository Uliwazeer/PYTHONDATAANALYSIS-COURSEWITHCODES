#ex1
import pandas as pd 
lst = [1000,2000,3000,4000,5000]
frame = pd.DataFrame(lst)
print("\n")
print(frame)
print("\n")
#ex2
import pandas as pd 
lst = [1000,2000,3000,4000,5000]
frame = pd.DataFrame(lst,index=['a','b','c','d','e'],columns=['first'])
print("\n")
print(frame)
print("\n")
#ex3
import pandas as pd 
lst = [1000,2000,3000,4000,5000]
frame = pd.DataFrame(lst,index=['a','b','c','d','e'],columns=['first'])
print("\n")
print(frame)
print(frame.index)
print(frame.values)
print(frame.columns)
print("\n")
#ex4
import pandas as pd 
lst = [1000,2000,3000,4000,5000]
frame = pd.DataFrame(lst,index=['a','b','c','d','e'],columns=['first'])
print("\n")
print(frame)
print(frame.describe())
#ex4
import pandas as pd 
lst = [1000,2000,3000,4000,5000]
frame = pd.DataFrame(lst,index=['a','b','c','d','e'],columns=['first'])
print("\n")
print(frame.agg(['mean','count']))
