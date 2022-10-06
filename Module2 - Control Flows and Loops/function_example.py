# This is a simple Python script.

def get_schoolyear() -> str:
    # Gets the school year for our person
    # based on specific possible answers
    years = ["freshman", "sophemore", "junior", "senior"]

    while True:
        # Give choices for school year and then return selected choice
        for i, e in enumerate(years):
            print(f"Enter {i} for {e}")

        choice = int(input("Enter a choice (0-4):"))
        if 0 <= choice <= 4:
            print("Thank you")
            return years[choice]


def get_verify_dob(year=1900) -> list:
    # get date of birth and ensure greater than 1
    # calculate age from dob and reprint
    while True:
        month = int(input("Please enter your month of birth (1-12): "))
        day = int(input("Please enter your day of birth (1-31): "))
        yearofbirth = int(input("Please enter your year of birth (YYYY: 2021): "))

        if (1 <= month <= 12) and (1 <= day <= 31) and (year < yearofbirth < 2022):
            print(f"You were born {month}/{day}/{yearofbirth} and are {2022 - yearofbirth} years old")
            return [month, day, yearofbirth]
        elif name == "bob":
            print("silly bob")
            return [0, 0, 0]
        else:
            print("Not the correct date")

# very simple input and print with if/else
if __name__ == '__main__':
    name = "J"
    yearofbirth = 1980
    schoolyear = ""

    # get user's name and greet them
    while True:
        name = input("Please enter your name: ")

        if input(f"Is {name.lower()} the correct name? (y/n)").startswith("y"):
            break

    print(f"Hi! Welcome {name}!")

    dob = get_verify_dob(1900)
    schoolyear = get_schoolyear()
