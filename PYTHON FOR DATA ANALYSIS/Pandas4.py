# ex1
import pandas as pd
lst1 = [10, 20, 30]
lst2 = [100, 200, 300]
lst3 = [1000, 2000, 3000]
df = pd.DataFrame([lst1, lst2, lst3], columns=["first", "second", "third"])
print(df)

# ex2
lst1 = ["ULI", 20000, 30500, +2001030568381]
lst2 = ["ULi", 25000, 30040, +2001030568382]
lst3 = ["ULy", 24000, 30003, +2001030568383]
lst4 = ["UL3", 23000, 30002, +2001030568384]
lst5 = ["UL2", 22000, 30001, +2001030568385]
df = pd.DataFrame([lst1, lst2, lst3, lst4, lst5], columns=[
                  "name", "income", "withdraw", "phone"])
print(df)
