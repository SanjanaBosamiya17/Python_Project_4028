import sqlite3

fields = []

n = int(input("Enter number of columns: "))

for i in range(n):
    name = input("Column Name: ")
    datatype = input("Data Type: ")
    size = input("Size: ")
    
    fields.append(f"{name} {datatype}({size})")

table_query = "CREATE TABLE new_table (" + ", ".join(fields) + ")"

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute(table_query)

print("Table created successfully!")

conn.commit()
conn.close()
