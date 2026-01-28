'''8. Write a Python program to perform following operation on given string input:
a) Count Number of Vowel in given string
b) Count Length of string (donot use len() )
c) Reverse string
d) Find and replace operation
e) check whether string entered is a palindrome or not'''


def main():
    s = input("Enter a string: ")
    
    print(f"\nString: '{s}'")
    
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    print(f"Vowels count: {vowel_count}")
    
    length = 0
    for _ in s:
        length += 1
    print(f"Length: {length}")
    
    reverse = s[::-1]
    print(f"Reversed: {reverse}")
    
    old = input("\nEnter text to find: ")
    new = input("Enter text to replace with: ")
    replaced = s.replace(old, new)
    print(f"After replacement: {replaced}")
    
    clean = ''.join(c.lower() for c in s if c.isalnum())
    is_pal = clean == clean[::-1]
    print(f"Is palindrome: {is_pal}")

if __name__ == "__main__":
    main()
