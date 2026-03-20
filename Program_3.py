class Student:
    # Class variable (shared by all instances)
    school = "Python High School"
    total_students = 0
    
    def __init__(self, name, age, grade):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.grade = grade
        Student.total_students += 1
    
    # Instance method (works with instance data)
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    # Instance method (can access instance variables)
    def update_grade(self, new_grade):
        self.grade = new_grade
        return f"{self.name}'s grade updated to {self.grade}"
    
    # Instance method (can access instance variables)
    def is_passing(self):
        return self.grade >= 60
    
    # Class method (works with class variables)
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        return f"School changed to: {cls.school}"
    
    # Class method (can access class variables)
    @classmethod
    def get_school_info(cls):
        return f"School: {cls.school}, Total Students: {cls.total_students}"
    
    # Class method (factory method - creates object using class method)
    @classmethod
    def create_freshman(cls, name, age):
        # Freshmen start with grade 50
        return cls(name, age, 50)
    
    # Another class method example
    @classmethod
    def get_student_count(cls):
        return f"Total students enrolled: {cls.total_students}"


# Let's use our class
print("=" * 50)
print("DEMONSTRATING INSTANCE AND CLASS METHODS")
print("=" * 50)

# Using class method without creating any instance
print("\n1. USING CLASS METHODS:")
print(Student.get_school_info())  # Output: School: Python High School, Total Students: 0

# Creating instances using regular constructor
print("\n2. CREATING INSTANCES:")
student1 = Student("Alice", 15, 85)
student2 = Student("Bob", 16, 45)

print(f"Created {student1.name} and {student2.name}")

# Using instance methods
print("\n3. USING INSTANCE METHODS:")
print(student1.display_info())  # Output: Name: Alice, Age: 15, Grade: 85
print(student2.display_info())  # Output: Name: Bob, Age: 16, Grade: 45

# Check if students are passing (instance method)
print(f"\n4. CHECKING PASSING STATUS:")
print(f"Is {student1.name} passing? {student1.is_passing()}")  # True
print(f"Is {student2.name} passing? {student2.is_passing()}")  # False

# Update grade using instance method
print("\n5. UPDATING GRADE:")
print(student2.update_grade(70))
print(f"After update - {student2.display_info()}")
print(f"Is {student2.name} passing now? {student2.is_passing()}")  # True

# Using class method to check school info
print("\n6. CLASS METHOD ACCESSING CLASS VARIABLES:")
print(Student.get_school_info())

# Using class method to change school
print("\n7. CHANGING SCHOOL USING CLASS METHOD:")
print(Student.change_school("Coding Academy"))
print(Student.get_school_info())

# Check that the change affects all instances
print(f"\n8. CHANGE AFFECTS ALL INSTANCES:")
print(f"{student1.name}'s school: {student1.school}")
print(f"{student2.name}'s school: {student2.school}")

# Using class method as factory method to create a freshman
print("\n9. USING CLASS METHOD AS FACTORY:")
freshman = Student.create_freshman("Charlie", 14)
print(freshman.display_info())  # Grade automatically set to 50

# Check total student count using class method
print("\n10. CHECKING TOTAL STUDENTS:")
print(Student.get_student_count())

'''
print("\n" + "=" * 50)
print("KEY POINTS TO REMEMBER:")
print("=" * 50)
print("• Instance methods need 'self' and work with instance data")
print("• Class methods need 'cls' and work with class data")
print("• Class methods use @classmethod decorator")
print("• Instance methods can access both instance and class data")
print("• Class methods can't access instance data directly")
print("• Use class methods for factory methods or modifying class state")
'''



