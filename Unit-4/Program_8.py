import matplotlib.pyplot as plt

courses = ["BCA", "MCA", "BSc IT", "MSc IT"]
students = [50, 70, 40, 60]

explode = [0, 0.1, 0, 0]

plt.pie(students, labels=courses, explode=explode, autopct='%1.1f%%')
plt.show()
