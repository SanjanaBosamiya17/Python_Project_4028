import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

roll = int(input("Roll No: "))
name = input("Name: ")
gender = input("Gender: ")
age = int(input("Age: "))
email = input("Email: ")
mobile = input("Mobile: ")
city = input("City: ")

cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)",
               (roll, name, gender, age, email, mobile, city))

conn.commit()
print("Record inserted successfully!")
conn.close()

