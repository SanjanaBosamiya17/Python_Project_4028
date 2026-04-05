import pandas as pd
import numpy as np

data = {
    "RollNo": range(1, 21),
    "Name": ["Amit", "Riya", "Karan", "Sneha", "Rahul", "Pooja", "Vikas", "Neha", "Arjun", "Priya",
             "Rohit", "Kajal", "Manish", "Nisha", "Yash", "Komal", "Jay", "Isha", "Dhruv", "Meena"],
    "Gender": ["Male", "Female"] * 10,
    "E-Mail": ["amit@gmail.com", "riya@", "karan@yahoo.com", "sneha@gmail.com", "rahul@", 
               "pooja@gmail.com", "vikas@gmail.com", "neha@", "arjun@gmail.com", "priya@gmail.com",
               "rohit@", "kajal@gmail.com", "manish@gmail.com", "nisha@", "yash@gmail.com",
               "komal@gmail.com", "jay@", "isha@gmail.com", "dhruv@gmail.com", "meena@"],
    "Mobile": ["91-9876543210", "9876543210", "91-9123456789", "9123456789", "91-9999999999",
               "9999999999", "91-8888888888", "8888888888", "91-7777777777", "7777777777",
               "91-6666666666", "6666666666", "91-5555555555", "5555555555", "91-4444444444",
               "4444444444", "91-3333333333", "3333333333", "91-2222222222", "2222222222"],
    "Age": np.random.randint(18, 25, 20),
    "City": ["Rajkot", "Ahmedabad", "Surat", "Rajkot", "Baroda",
             "Rajkot", "Surat", "Ahmedabad", "Rajkot", "Baroda",
             "Rajkot", "Surat", "Ahmedabad", "Rajkot", "Baroda",
             "Rajkot", "Surat", "Ahmedabad", "Rajkot", "Baroda"]
}

df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)

print("Excel file created successfully!")
