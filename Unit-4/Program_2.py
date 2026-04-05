import pandas as pd

df = pd.read_excel("students.xlsx")

print(df[df["City"] == "Rajkot"])
print(df[df["Gender"] == "Male"])
print(df[(df["Gender"] == "Male") & (df["City"] == "Rajkot")])
print(df[df["Age"] >= 20])
