# PROGRAM 10: Zip and Unzip Files
# ============================================================
import zipfile
 
def prog10():
    print("\n=== Program 10: Zip and Unzip ===")
 
    # Create sample files to zip
    for name, text in [("file1.txt","Hello from file1"), ("file2.txt","Hello from file2")]:
        with open(name, "w") as f: f.write(text)
 
    # ZIP
    with zipfile.ZipFile("archive.zip", "w") as z:
        z.write("file1.txt")
        z.write("file2.txt")
    print("Files zipped into archive.zip")
 
    # UNZIP
    os.makedirs("unzipped", exist_ok=True)
    with zipfile.ZipFile("archive.zip", "r") as z:
        z.extractall("unzipped")
    print("Unzipped to 'unzipped/' folder")
    print("Contents:", os.listdir("unzipped"))
