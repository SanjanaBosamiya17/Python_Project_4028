import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM student")

while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)

conn.close()
