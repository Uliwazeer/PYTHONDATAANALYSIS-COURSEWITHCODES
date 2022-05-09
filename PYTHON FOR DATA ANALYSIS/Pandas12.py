# EX1
import pandas as pd
import pandas as pd
data = pd.read_csv('datafile.csv')
print(data)
# EX2 if you want to remove all header
data = pd.read_csv('datafile.csv', header=None)
print(data)
# EX3 if you want to give column names instead of given
data = pd.read_csv('datafile.csv', header=None,
                   names=["A", "B", "C", "D", "E"])
print(data)
# EX4
data = pd.read_csv('datafile.csv'header=0)
print(data)
# EX5
data = pd.read_csv('datafile.csv'header=1)
print(data)
# EX6 to store all data modified in file excel
data = pd.read_csv('datafile.csv', header=0)
data.insert(0, "test", 1)
print(data)
data.to_csv('datafile_new.csv')
print(data)
# EX7 to read file with extension xls

data = pd.ExcelFile('datafile.xls')
table = data.parset('sheet_1')
print(table)
