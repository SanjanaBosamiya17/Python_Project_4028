# PROGRAM 3: Arithmetic Exception with Logging
# ============================================================
import logging
 
logging.basicConfig(
    filename="exception.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
def prog3():
    print("=== Program 3: Arithmetic Exception + Logging ===")
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        print(f"Result: {a / b}")
    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError: {e}")
        print("Error: Cannot divide by zero! (Logged)")
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        print("Error: Enter valid integers! (Logged)")
