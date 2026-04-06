import sqlite3

roll = int(input("Enter Roll No to search: "))

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM student WHERE rollno=?", (roll,))
row = cursor.fetchone()

if row:
    print("Student Found:", row)
else:
    print("Student not found")

conn.close()
