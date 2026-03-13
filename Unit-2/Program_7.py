# PROGRAM 7: Copy a Text File
# ============================================================
def prog7():
    print("\n=== Program 7: Copy Text File ===")
    with open("source.txt", "w") as f:
        f.write("This is the source file.\nCopying this content.")
 
    with open("source.txt", "r") as src, open("destination.txt", "w") as dst:
        dst.write(src.read())
 
    print("File copied successfully!")
    with open("destination.txt", "r") as f:
        print("Destination file:\n", f.read())
