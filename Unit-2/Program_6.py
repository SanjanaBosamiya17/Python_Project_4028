# PROGRAM 6: Numbers File - Total, Max, Min
# ============================================================
def prog6():
    print("\n=== Program 6: Numbers File - Total, Max, Min ===")
    with open("numbers.txt", "w") as f:
        f.write("10\n25\n3\n78\n45\n99\n12\n56")
 
    with open("numbers.txt", "r") as f:
        nums = [int(line.strip()) for line in f if line.strip()]
 
    print(f"Numbers : {nums}")
    print(f"Total   : {sum(nums)}")
    print(f"Maximum : {max(nums)}")
    print(f"Minimum : {min(nums)}")
