# PROGRAM 4: Module with 4 Functions (defined & used here)
# ============================================================
def add(a, b):       return a + b
def factorial(n):    return 1 if n <= 1 else n * factorial(n - 1)
def is_palindrome(s): return s == s[::-1]
def celsius_to_f(c): return (c * 9/5) + 32
 
def prog4():
    print("\n=== Program 4: Module Functions ===")
    print("add(5,3)         =", add(5, 3))
    print("factorial(5)     =", factorial(5))
    print("is_palindrome('madam') =", is_palindrome("madam"))
    print("celsius_to_f(100)=", celsius_to_f(100))
 
