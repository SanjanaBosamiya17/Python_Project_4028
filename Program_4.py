# Super simple inner class example
class School:
    class Student:
        def __init__(self, name):
            self.name = name
    
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
    
    def add_student(self, name):
        student = self.Student(name)
        self.students.append(student)
        return f"Added {name}"

# Test it
my_school = School("ABC School")
print(my_school.add_student("Alice"))
print(my_school.add_student("Bob"))
print(f"Students: {[s.name for s in my_school.students]}")
