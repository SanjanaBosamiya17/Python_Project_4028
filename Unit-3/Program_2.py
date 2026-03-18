class Student:
    """
    Student class with RollNo, Name, Age, Gender attributes
    and methods to add and display student information
    """
    
    def __init__(self):
        """Constructor to initialize student attributes"""
        self.roll_no = None
        self.name = None
        self.age = None
        self.gender = None
        print("Student object created!")
    
    def AddStudent(self):
        """Method to add student information"""
        print("\n--- Enter Student Details ---")
        self.roll_no = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender: ")
        print("Student information added successfully!")
    
    def DisplayStudent(self):
        """Method to display student information"""
        print("\n--- Student Details ---")
        print(f"Roll Number: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print("----------------------")


# Main program to demonstrate the Student class
def main():
    # Create a student object
    student1 = Student()
    
    # Add student information
    student1.AddStudent()
    
    # Display student information
    student1.DisplayStudent()
    
    # Create and process another student
    print("\n" + "="*30)
    print("Processing second student")
    print("="*30)
    
    student2 = Student()
    student2.AddStudent()
    student2.DisplayStudent()


# Run the main program
if __name__ == "__main__":
    main()
