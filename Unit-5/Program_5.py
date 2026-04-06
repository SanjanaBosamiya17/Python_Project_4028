import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

roll = int(input("Enter Roll No to update: "))
new_city = input("Enter new city: ")

cursor.execute("UPDATE student SET city=? WHERE rollno=?", (new_city, roll))

conn.commit()

if cursor.rowcount > 0:
    print("Record updated successfully!")
else:
    print("Student not found")

conn.close()
