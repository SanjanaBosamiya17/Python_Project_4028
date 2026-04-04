class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def show_student(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Age:", self.age)


class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        Student.__init__(self, rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def show_course(self):
        self.show_student()
        print("Course Name:", self.coursename)
        print("Duration:", self.duration)
        print("Fee:", self.fee)


c1 = Course(101, "Rahul", "Male", 20, "Python", "3 Months", 5000)
c1.show_course()
