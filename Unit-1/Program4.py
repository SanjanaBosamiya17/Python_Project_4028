#write a program to enter 10 numbers and display armstrong numbers from those numbers.

def is_armstrong(num):
    digits = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num


numbers = []
print("Enter 10 numbers:")
for i in range(10):
    n = int(input())
    numbers.append(n)

print("\nArmstrong numbers are:")
for num in numbers:
    if is_armstrong(num):
        print(num)
