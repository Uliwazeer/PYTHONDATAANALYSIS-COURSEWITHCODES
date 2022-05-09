# ex1
import pandas as pd 
ser = pd.Series(['A','B','C','D','E'])
print("\n")
print(ser.unique())
print("\n")
# ex2
import pandas as pd 
lst1 = ["ALI",2000,"L",1500,"lst1@example.com",'YES']
lst2 = ["ALY",2200,"K",1560,"lst2@example.com",'YES']
lst3 = ["ULI",2300,"J",1570,"lst3@example.com",'NO']
lst4 = ["ALU",2400,"H",1580,"lst4@example.com",'YES']
lst5 = ["AL3",2500,"G",1590,"lst5@example.com",'NO']

df = pd.DataFrame([lst1,lst2,lst3,lst4,lst5],index=['A','B','C','D','E'],columns=["NAME","INCOME","CLASS","WITHDRAW","E-MAIL","ACTIVE"])
print("\n")
print(df)
print(df["NAME"])
print(df["CLASS"])
print(df["INCOME"])
print(df["E-MAIL"])
print(df["ACTIVE"])
# ex3
import pandas as pd 
lst1 = ["ALI",2000,"L",1500,"lst1@example.com",'YES']
lst2 = ["ALY",2200,"K",1560,"lst2@example.com",'YES']
lst3 = ["ULI",2300,"J",1570,"lst3@example.com",'NO']
lst4 = ["ALU",2400,"H",1580,"lst4@example.com",'YES']
lst5 = ["AL3",2500,"G",1590,"lst5@example.com",'NO']

df = pd.DataFrame([lst1,lst2,lst3,lst4,lst5],index=['A','B','C','D','E'],columns=["NAME","INCOME","CLASS","WITHDRAW","E-MAIL","ACTIVE"])
print("\n")
print(df)
print(df["NAME","CLASS","E-MAIL"])
print(df["NAME","CLASS","E-MAIL"].describe())
print(df.agg([]))
print(df.loc["L":"H","INCOME":"E-MAIL"])#TO MAKING CUT FOR SOME DATA(RAWS, COLUMN)
# ex4 if we remove index from df and put numbers when printing
import pandas as pd 
lst1 = ["ALI",2000,"L",1500,"lst1@example.com",'YES']
lst2 = ["ALY",2200,"K",1560,"lst2@example.com",'YES']
lst3 = ["ULI",2300,"J",1570,"lst3@example.com",'NO']
lst4 = ["ALU",2400,"H",1580,"lst4@example.com",'YES']
lst5 = ["AL3",2500,"G",1590,"lst5@example.com",'NO']

df = pd.DataFrame([lst1,lst2,lst3,lst4,lst5],columns=["NAME","INCOME","CLASS","WITHDRAW","E-MAIL","ACTIVE"])
print("\n")
print(df)
print(df["NAME","CLASS","E-MAIL"])
print(df["NAME","CLASS","E-MAIL"].describe())
print(df.agg([]))
print(df.loc["1":"4","INCOME":"E-MAIL"])#TO MAKING CUT FOR SOME DATA(RAWS, COLUMN)
# ex5 if we remove index from df and put numbers when printing
import pandas as pd 
lst1 = ["ALI",2000,"L",1500,"lst1@example.com",'YES']
lst2 = ["ALY",2200,"K",1560,"lst2@example.com",'YES']
lst3 = ["ULI",2300,"J",1570,"lst3@example.com",'NO']
lst4 = ["ALU",2400,"H",1580,"lst4@example.com",'YES']
lst5 = ["AL3",2500,"G",1590,"lst5@example.com",'NO']

df = pd.DataFrame([lst1,lst2,lst3,lst4,lst5],columns=["NAME","INCOME","CLASS","WITHDRAW","E-MAIL","ACTIVE"])
print("\n")

print(df.loc[ :"4","INCOME":"E-MAIL"])#TO MAKING CUT FOR SOME DATA(RAWS, COLUMN)
# ex6 if we remove index from df and put numbers when printing
import pandas as pd 
lst1 = ["ALI",2000,"L",1500,"lst1@example.com",'YES']
lst2 = ["ALY",2200,"K",1560,"lst2@example.com",'YES']
lst3 = ["ULI",2300,"J",1570,"lst3@example.com",'NO']
lst4 = ["ALU",2400,"H",1580,"lst4@example.com",'YES']
lst5 = ["AL3",2500,"G",1590,"lst5@example.com",'NO']

df = pd.DataFrame([lst1,lst2,lst3,lst4,lst5],columns=["NAME","INCOME","CLASS","WITHDRAW","E-MAIL","ACTIVE"])
print("\n")

print(df.loc["2" :,"INCOME":"E-MAIL"])#TO MAKING CUT FOR SOME DATA(RAWS, COLUMN)
# ex7 if we remove index from df and put numbers when printing
import pandas as pd 
lst1 = ["ALI",2000,"L",1500,"lst1@example.com",'YES']
lst2 = ["ALY",2200,"K",1560,"lst2@example.com",'YES']
lst3 = ["ULI",2300,"J",1570,"lst3@example.com",'NO']
lst4 = ["ALU",2400,"H",1580,"lst4@example.com",'YES']
lst5 = ["AL3",2500,"G",1590,"lst5@example.com",'NO']

df = pd.DataFrame([lst1,lst2,lst3,lst4,lst5],columns=["NAME","INCOME","CLASS","WITHDRAW","E-MAIL","ACTIVE"])
print("\n")

print(df.loc["2" : , :"E-MAIL"])#TO MAKING CUT FOR SOME DATA(RAWS, COLUMN) location=>loc
# ex8 if we remove index from df and put numbers when printing
import pandas as pd 
lst1 = ["ALI",2000,"L",1500,"lst1@example.com",'YES']
lst2 = ["ALY",2200,"K",1560,"lst2@example.com",'YES']
lst3 = ["ULI",2300,"J",1570,"lst3@example.com",'NO']
lst4 = ["ALU",2400,"H",1580,"lst4@example.com",'YES']
lst5 = ["AL3",2500,"G",1590,"lst5@example.com",'NO']

df = pd.DataFrame([lst1,lst2,lst3,lst4,lst5],columns=["NAME","INCOME","CLASS","WITHDRAW","E-MAIL","ACTIVE"])
print("\n")
# index location=>(iloc)
print(df.iloc[1:3 , 2:5])#TO MAKING CUT FOR SOME DATA(RAWS, COLUMN) location=>loc