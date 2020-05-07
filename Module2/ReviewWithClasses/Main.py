from .UnitConversion import UnitConversion
# Above from "." = current directory

try:
    user_feet = float(input("Please enter the number of feet (0 or greater)"))
    user_inches = float(input("Please enter the number of inches (0 or greater)"))
    # This could ask for both and split on a space but with a console better to split it
except ValueError:
    print("You must enter a numeric value for feet & inches")
    user_feet = 0.0
    user_inches = 0.0

uc = UnitConversion(user_feet, user_inches)
uc.set_all()
print(uc)

