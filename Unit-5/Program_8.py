import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

for row in rows:
    name = row[1]
    if name.startswith('N') and len(name) == 5:
        print(row)

conn.close()
