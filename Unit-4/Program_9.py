import pandas as pd
import re

df = pd.read_excel("students.xlsx")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

print(df[df["E-Mail"].str.match(pattern, na=False)])
