import sqlite3

def insert():
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
    conn.close()
    print("Inserted!")

def update():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    
    roll = int(input("Roll No: "))
    city = input("New City: ")
    
    cursor.execute("UPDATE student SET city=? WHERE rollno=?", (city, roll))
    
    conn.commit()
    conn.close()
    print("Updated!")

def search():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    
    roll = int(input("Roll No: "))
    
    cursor.execute("SELECT * FROM student WHERE rollno=?", (roll,))
    row = cursor.fetchone()
    
    if row:
        print(row)
    else:
        print("Not found")
    
    conn.close()

def delete():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    
    roll = int(input("Roll No: "))
    
    cursor.execute("DELETE FROM student WHERE rollno=?", (roll,))
    
    conn.commit()
    conn.close()
    print("Deleted!")

def display():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM student")
    
    for row in cursor.fetchall():
        print(row)
    
    conn.close()

while True:
    print("\n1.Insert 2.Update 3.Search 4.Delete 5.List 6.Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 1:
        insert()
    elif ch == 2:
        update()
    elif ch == 3:
        search()
    elif ch == 4:
        delete()
    elif ch == 5:
        display()
    elif ch == 6:
        break
    else:
        print("Invalid choice")
