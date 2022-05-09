# ex1
# dropna()=>remove any column contains have a not complete information
import pandas as pd

lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5,None]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5,None]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
new_data = df.dropna()
print(new_data)
# if you want to remove value and add other using =>fillna
df.fillna("AL",inplace=true)#note this function not store in varible
df.fillna(0,inplace=true)#note this function not store in varible will replace npne with 0
print(df)
# ex2
# dropna()=>remove any column contains have a not complete information
import pandas as pd

lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5,None]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5,None]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
new_data = df.dropna()
print(new_data)
print(df)
# if you want to replace a value in some row limit this row and 
df["E-MAIL"].fillna("UNKNOWN",inplace=true) #replace any empty value with Word UNKNOWN
print(df)
# replace any empty value with Word FOLLOW
df["CLASS"].fillna("FOLLOW", inplace=true)
print(df)
print("\n")
print(df.dtypes)
print(df)
