# ex1
import pandas as pd
data1 = [['Ali', 21],
         ['Ahmad', 22],
         ['Awad', 23],
         ['Noour', 24],
         ['Wazeer', 25]
         ]
data2 = [['Engineer'], ['Accountant'], ['Developer'], ['Cheif'], ['Student']]
df1 = pd.DataFrame(data1, columns=['Name', 'Age'])
df2 = pd.DataFrame(data2, columns=['Job'])
print(df1)
print(df2)
# to concate data1 with data2 using this function which called concate() axis=1 concate data1 with data2 as column
# to concate data1 with data2 using this function which called concate() axis=0 concate data1 with data2 as row
con1 = pd.concat([df1,df2],axis=1)
con2 = pd.concat([df1,df2],axis=0)
print(con1)
print(con2)
# ex2 insert(index,column name,value)
import pandas as pd
data1 = [['Ali', 21],
         ['Ahmad', 22],
         ['Awad', 23],
         ['Noour', 24],
         ['Wazeer', 25]
         ]
data2 = [['Engineer'], ['Accountant'], ['Developer'], ['Cheif'], ['Student']]
df1 = pd.DataFrame(data1, columns=['Name', 'Age'])
df2 = pd.DataFrame(data2, columns=['Job'])
print(df1)
print(df2)
df1.insert(0,'Level',0)
print(df1)
# ex3 insert(index,column name,value)
import pandas as pd
data1 = [['Ali', 21],
         ['Ahmad', 22],
         ['Awad', 23],
         ['Noour', 24],
         ['Wazeer', 25]
         ]
data2 = [['Engineer'], ['Accountant'], ['Developer'], ['Cheif'], ['Student']]
df1 = pd.DataFrame(data1, columns=['Name', 'Age'])
df2 = pd.DataFrame(data2, columns=['Job'])
print(df1)
print(df2)
df1.insert(0,'Level',"Uli")
print(df1)
# ex4 insert(index,column name,value)
import pandas as pd
data1 = [['Ali', 21],
         ['Ahmad', 22],
         ['Awad', 23],
         ['Noour', 24],
         ['Wazeer', 25]
         ]
data2 = [['Engineer'], ['Accountant'], ['Developer'], ['Cheif'], ['Student']]
df1 = pd.DataFrame(data1, columns=['Name', 'Age'])
df2 = pd.DataFrame(data2, columns=['Job'])
print(df1)
print(df2)
df1.insert(0,'Level',[1,2,3,4,5])
print(df1)