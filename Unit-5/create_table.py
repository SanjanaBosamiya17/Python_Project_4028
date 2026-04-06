import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    rollno INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    age INTEGER,
    email TEXT,
    mobile TEXT,
    city TEXT
)
""")

print("Table created successfully!")

conn.commit()
conn.close()
