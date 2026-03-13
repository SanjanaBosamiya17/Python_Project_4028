# PROGRAM 9: Student CRUD Operations (File-based Menu)
# ============================================================
import os
 
FILE = "students.txt"
 
def load():
    if not os.path.exists(FILE): return []
    with open(FILE) as f:
        return [line.strip().split(",") for line in f if line.strip()]
 
def save(students):
    with open(FILE, "w") as f:
        for s in students:
            f.write(",".join(s) + "\n")
 
def prog9():
    print("\n=== Program 9: Student Operations ===")
    while True:
        print("\na)Add  b)Search  c)List  d)Update  e)Delete  f)Exit")
        ch = input("Choice: ").lower()
 
        if ch == 'a':
            r, n = input("Roll: "), input("Name: ")
            students = load(); students.append([r, n]); save(students)
            print("Student added!")
 
        elif ch == 'b':
            r = input("Enter Roll to search: ")
            found = [s for s in load() if s[0] == r]
            print(found[0] if found else "Not found!")
 
        elif ch == 'c':
            students = load()
            if students:
                [print(f"Roll:{s[0]}  Name:{s[1]}") for s in students]
            else:
                print("No students found.")
 
        elif ch == 'd':
            r, n = input("Roll to update: "), input("New Name: ")
            students = load()
            for s in students:
                if s[0] == r: s[1] = n
            save(students); print("Updated!")
 
        elif ch == 'e':
            r = input("Roll to delete: ")
            students = [s for s in load() if s[0] != r]
            save(students); print("Deleted!")
 
        elif ch == 'f':
            print("Exiting..."); break
        else:
            print("Invalid choice!")
