import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

roll = int(input("Enter Roll No to delete: "))

cursor.execute("DELETE FROM student WHERE rollno=?", (roll,))

conn.commit()

if cursor.rowcount > 0:
    print("Record deleted successfully!")
else:
    print("Student not found")

conn.close()
