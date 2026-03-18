class SimpleClass:
    """
    A simple class with 2 methods
    """
    
    def __init__(self, name):
        """Constructor method - initializes the object"""
        self.name = name
        print(f"Object created for {self.name}")
    
    def method_one(self):
        """First method - displays a greeting"""
        print(f"Hello from method one! This is {self.name}")
        print("Method one is executing...")
    
    def method_two(self):
        """Second method - performs a simple calculation"""
        print(f"Hello from method two! This is {self.name}")
        print("Method two is executing...")
        
        # Simple calculation example
        numbers = [1, 2, 3, 4, 5]
        total = sum(numbers)
        print(f"Sum of {numbers} is: {total}")


# Create an instance of the class
my_object = SimpleClass("MySimpleObject")

# Execute both methods
print("\n--- Executing Method One ---")
my_object.method_one()

print("\n--- Executing Method Two ---")
my_object.method_two()

print("\n--- Program completed ---")
