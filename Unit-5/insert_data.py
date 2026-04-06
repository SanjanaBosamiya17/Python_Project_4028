import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

students = [
    (1, "Neha", "Female", 21, "neha@gmail.com", "91-9876543210", "Rajkot"),
    (2, "Nisha", "Female", 22, "nisha@gmail.com", "91-9123456789", "Ahmedabad"),
    (3, "Amit", "Male", 20, "amit@gmail.com", "91-9999999999", "Surat"),
    (4, "Nilesh", "Male", 23, "nilesh@gmail.com", "91-8888888888", "Rajkot"),
    (5, "Kiran", "Male", 19, "kiran@", "9999999999", "Baroda")
]

cursor.executemany("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)", students)

conn.commit()
print("Data inserted successfully!")

conn.close()
