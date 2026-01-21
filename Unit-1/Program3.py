#3. Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)
print("------STUDENT RESULT-------")
java=int(input("Enter the JAVA Language Marks="))
dsa=int(input("Enter the DSA Language Marks="))
c=int(input("Enter the C Langauge Marks="))
python=int(input("Enter the Python Langauge Marks="))

total=(java+dsa+c+python)
print("Total=",total)

average=(total/4)
print("Average=",average)

if average>=40:
    print("Congraluation you Passed")

    if average>=90:
        print("Grade A+")
    elif average>=80:
        print("Grade A")
    elif average>=70:
        print("Grade B")
    elif average>=60:
        print("Grade C")
    elif average>=50:
        print("Grade D")
    else:
        print("Grade E")
else:
    print("You Failed in Exam,Better Luck Next Time")
