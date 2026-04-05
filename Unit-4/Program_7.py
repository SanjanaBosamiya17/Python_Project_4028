import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("students.xlsx")

count = df["Gender"].value_counts()

plt.bar(count.index, count.values)
plt.show()
