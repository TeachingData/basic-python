# This is a simple Python script used to demo basic principles from variables to if


# very simple input and print with if/else
if __name__ == '__main__':
    name = "J"
    yearofbirth = 1980

    # get user's name and greet them
    name = input("Please enter your name: ")
    print(f"Hi! Welcome {name}!")

    # get date of birth and ensure greater than 1
    # calculate age from dob and reprint
    month = int(input("Please enter your month of birth (1-12): "))
    day = int(input("Please enter your day of birth (1-31): "))
    yearofbirth = int(input("Please enter your year of birth (2021 or earlier): "))

    if (1 <= month <= 12) and (1 <= day <= 31) and (0 < yearofbirth < 2022):
        age = 2022 - yearofbirth
        print(f"You were born {month}/{day}/{yearofbirth} and are {age} years old")
    elif name == "bob":
        print("silly bob")
    else:
        print("Not the correct date")
