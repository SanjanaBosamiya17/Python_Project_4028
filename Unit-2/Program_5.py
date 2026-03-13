# PROGRAM 5: Read File & Count Words
# ============================================================
def prog5():
    print("\n=== Program 5: Read File & Word Count ===")
    # Create a sample file
    with open("sample.txt", "w") as f:
        f.write("Python is great\nFile handling is easy\nHello World")
 
    with open("sample.txt", "r") as f:
        content = f.read()
 
    print(content)
    print("-----------------------------")
    print(f"Total Words: {len(content.split())}")
 
