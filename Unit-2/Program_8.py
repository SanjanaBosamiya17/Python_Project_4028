# PROGRAM 8: Student Marks - Total, Percentage, Grade
# ============================================================
def prog8():
    print("\n=== Program 8: Student Marks ===")
    with open("marks.csv", "w") as f:
        f.write("RollNo,Name,Mark1,Mark2,Mark3,Mark4\n")
        f.write("1,Alice,85,90,78,92\n")
        f.write("2,Bob,55,60,58,62\n")
        f.write("3,Charlie,40,35,45,38\n")
 
    def grade(p):
        if p >= 75: return "A"
        elif p >= 60: return "B"
        elif p >= 50: return "C"
        elif p >= 40: return "D"
        else: return "F"
 
    with open("marks.csv", "r") as f:
        lines = f.readlines()[1:]  # skip header
 
    print(f"{'Roll':<6}{'Name':<12}{'Total':<8}{'Percent':<10}{'Grade'}")
    print("-" * 42)
    for line in lines:
        r, n, m1, m2, m3, m4 = line.strip().split(",")
        total = int(m1) + int(m2) + int(m3) + int(m4)
        perc  = total / 4
        print(f"{r:<6}{n:<12}{total:<8}{perc:<10.2f}{grade(perc)}")
