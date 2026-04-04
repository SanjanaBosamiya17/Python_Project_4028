class Number:
    def __init__(self, value):
        self.value = value

    # overloading + operator
    def __add__(self, other):
        result = self.value + other.value
        return Number(result)

    # overloading - operator
    def __sub__(self, other):
        result = self.value - other.value
        return Number(result)

    def show(self):
        print("Value:", self.value)


n1 = Number(50)
n2 = Number(30)

print("First Number:")
n1.show()

print("Second Number:")
n2.show()

add_result = n1 + n2
print("After Addition:")
add_result.show()

sub_result = n1 - n2
print("After Subtraction:")
sub_result.show()
