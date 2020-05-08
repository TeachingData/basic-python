from .PyConversion import UnitConversion
# Above from "." = current directory

try:
    user_inches = float(input("Please enter the number of inches (0 or greater)"))
except ValueError:
    print("You must enter a numeric value for inches")
    user_inches = 0.0

uc = UnitConversion(user_inches)
print(f"I just want to know that yards = {uc.yards}")
print(f"Actually: print the whole thing\n {uc}")

