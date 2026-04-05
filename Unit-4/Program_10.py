import pandas as pd
import re

df = pd.read_excel("students.xlsx")

pattern = r'^\d{2}-\d{10}$'

print(df[df["Mobile"].str.match(pattern, na=False)])
