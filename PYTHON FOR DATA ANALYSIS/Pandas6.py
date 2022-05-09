# ex1
import pandas as pd

lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
# if there are column you wnt to remove it use drop()
# ex2

lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
# axis=1 meaning column will removed
new_df = df.drop(["SCORE", "E-MAIL", "NAME"], axis=1)
# if axis = 0 meaning rows will removed
print(new_df)
# ex3
# when you want to remove rows
lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
# axis=1 meaning column will removed
new_df = df.drop(["SCORE", "E-MAIL", "NAME"], axis=0)
# if axis = 0 meaning rows will removed
print(new_df)
# ex4
# when you want to remove rows
lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
# axis=1 meaning column will removed
new_df = df.drop(["K", "L"], axis=0)
# if axis = 0 meaning rows will removed
print(new_df)
# ex5
# when you want to remove rows
lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
# axis=1 meaning column will removed
new_df = df.drop([1, 3], axis=0)
# if axis = 0 meaning rows will removed
print(new_df)
# ex6
# TO KHNOW THE DATATYPE
# when you want to remove rows
lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
# axis=1 meaning column will removed
new_df = df.drop([1, 3], axis=0)
# if axis = 0 meaning rows will removed
print(new_df)
dt = df.dtypes
print(dt)
# ex7
# TO KHNOW all DATATYPE with its type
# when you want to remove rows
lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
# type of data which include object
dt_select1 = df.select_dtypes(include=['object'])
print(dt_select1)
# type of data which include integer
dt_select2 = df.select_dtypes(include=['int64'])
print(dt_select2)
# ex8
# TO KHNOW all DATATYPE with its type
# when you want to remove rows
lst1 = ["ALI", 2000, "L", 1500, "lst1@example.com", 'YES', 3.5]
lst2 = ["ALY", 2200, "K", 1560, "lst2@example.com", 'YES', 4.5]
lst3 = ["ULI", 2300, "J", 1570, "lst3@example.com", 'NO', 5.5]
lst4 = ["ALU", 2400, "H", 1580, "lst4@example.com", 'YES', 6.5]
lst5 = ["AL3", 2500, "G", 1590, "lst5@example.com", 'NO', 7.5]

df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], index=['A', 'B', 'C', 'D', 'E'], columns=[
                  "NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "ACTIVE", "SCORE"])
print("\n")
print(df)
# type of data which exclude object
dt_select1 = df.select_dtypes(exclude=['object'])
print(dt_select1)
# type of data which exclude integer
dt_select2 = df.select_dtypes(exclude=['int64'])
print(dt_select2)
