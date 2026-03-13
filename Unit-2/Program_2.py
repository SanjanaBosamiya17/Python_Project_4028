# User Defined Exception in Python

class AgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be between 1 and 120.")

# Main program
try:
    age = int(input("Enter age: "))
    if age < 1 or age > 120:
        raise AgeError(age)
    print(f"Valid age: {age}")

except AgeError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Please enter a number!")
```

**Output (examples):**
```
# Case 1 - Valid age
Enter age: 25
Valid age: 25

# Case 2 - Invalid age (user defined exception)
Enter age: 200
Error: Invalid age: 200. Age must be between 1 and 120.

# Case 3 - Non-numeric input
Enter age: abc
Error: Please enter a number!
