import sqlite3
import re

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

for row in rows:
    if re.match(pattern, row[4]):
        print(row)

conn.close()
