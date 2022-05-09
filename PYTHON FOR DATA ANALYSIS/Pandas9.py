# ex1
from traceback import print_tb
import pandas as pd 
team = [ 
        ['Ali','Engineer'],
        ['Aly','Maneger'],
        ['Uli','Software'],
        ['Alaa','Developer'],
        ['Alia','Accountant']
        ]
age = [ 
        ['Ali',20],
        ['Aly',21],
        ['Uli',22],
        ['Alaa',23],
        ['Alia',24]
        ]
# function concate() was repeat rows or columns
# function merge() dont repeat rows or columns
df_team = pd.DataFrame(team,columns="Name","Job")
df_age = pd.DataFrame(age,columns="Name","Age")
print("\n")
print(df_team)
print("\n")
print(df_age)
# ex2 using function merge() to concate column or rows together
# function merge() dont repeat rows or columns #notes should anything لازم يكون البيانات مشتركة ف نوعي البيانات اللي هندمجهم معا
import pandas as pd 
team = [ 
        ['Ali','Engineer'],
        ['Aly','Maneger'],
        ['Uli','Software'],
        ['Alaa','Developer'],
        ['Alia','Accountant']
        ]
age = [ 
        [22,20],
        [258,21],
        [248,22],
        [789,23],
        [5489,24]
        ]
# function concate() was repeat rows or columns
# function merge() dont repeat rows or columns #notes should anything لازم يكون البيانات مشتركة ف نوعي البيانات اللي هندمجهم معا
df_team = pd.DataFrame(team,columns="Name","Job")
df_age = pd.DataFrame(age,columns="Salary","Age")
print("\n")
print(df_team)
print("\n")
print(df_age)
new_df = pd.merge(df_team,df_age)
print(new_df)#print df_team and df_age لما ييجي يعمل ميرج هيطلع خطا علشان مفيش حاجة مشتركة بينهمولازم يكونو مكتبين بنفس حروف كابيتل او اسمووول

# ex2 using function merge() to concate column or rows together
from traceback import print_tb
import pandas as pd 
team = [ 
        ['Ali','Engineer'],
        ['Aly','Maneger'],
        ['Uli','Software'],
        ['Alaa','Developer'],
        ['Alia','Accountant']
        ]
age = [ 
        ['Ali',20],
        ['Aly',21],
        ['Uli',22],
        ['Alaa',23],
        ['Alia',24]
        ]
# function concate() was repeat rows or columns
# function merge() dont repeat rows or columns #notes should anything لازم يكون البيانات مشتركة ف نوعي البيانات اللي هندمجهم معا
df_team = pd.DataFrame(team,columns="Name","Job")
df_age = pd.DataFrame(age,columns="Name","Age")
print("\n")
print(df_team)
print("\n")
print(df_age)
new_df = pd.merge(df_team,df_age)
print(new_df)

