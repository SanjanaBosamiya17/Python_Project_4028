import pandas as pd

df = pd.read_excel("students.xlsx")

df.loc[0, "Age"] = None

print(df.dropna())
print(df.fillna(0))
