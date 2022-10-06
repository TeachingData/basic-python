# This was used to teach Python: version does not have final function and uses list for reciept
# few "constants" (tiprate is base tip percentage for first suggestion)
# MENU is the base menu with spacing added for template printing
TAXRATE = .065
TIPRATE = .18
MENU = {"slice of pizza": 534,
        "hamburger": 483,
        "fries": 250,
        "drink": 125}


def check_exit(phrase:str="Do you have more items to add?", flag:str="y"):
    """
    This asks the passed question or phrase and then ensures the flag is the first letter of response.
    :param phrase: The phrase to ask or propose
    :param flag: The True value to check as first letter or letters
    :return: Bool response to check
    """
    return input(phrase).lower().startswith(flag.lower())


def get_tip(total: int) -> int:
    """
    Suggest and then return the total tip the client wants to add
    :param total: the total without tip, integer because cents not dollars
    :return: the tip calculated with user input and total price
    """
    tip = input(f"Your suggested tip is ${total * TIPRATE/100:.2f}\nPlease enter your tip: $")
    # if tip is cents (.99 - .01) we just round to 0
    if tip < "0":
        tip = 0
    tip = int(float(tip) * 100)
    return tip

# list for transaction costs
# we are going to use ints for our prices because its better
selection = []
total = 0

# Will now loop until client enters all prices
# Check if client wants to add more items and then add items while checking price
while True:
    # print items available to add to our order
    print("\n--------------------")
    for food, price in MENU.items():
        print(f"{food.capitalize():14}\t${price/100:.2f}")

    if check_exit("Please select from the following:\n1: <add> an item\n2: <done>\n> ", "1"):
        item = input("Which item do you wish to add?").lower().strip()

        if item in MENU:
            item_price = MENU[item]
        else:
            print("Not a valid menu choice")
            continue

        selection.append([item, item_price])
        total += item_price
    else:
        break

# check if prices exists and exit if not
if not selection:
    print("Thank you for visiting us!")
    quit()

# print out receipt with gotten tip and totals
# tax set using TAXRATE constant and we loop over list for better UI
print("--------------------------\n\nYour reciept is:")
for food in selection:
    print(f"{food[0]:14}\t${food[1]/100:.2f}")

# calculate tax and total with tax then tip from client
tax = total * TAXRATE
total_and_tax = total + tax
print(f"The total is ${total/100:.2f} with taxes of ${tax/100:.2f}.")
print(f"For a full total of ${total_and_tax/100:.2f}")

tip = get_tip(total)
print(f"With tip of {tip/100:.2f} your total is {(total_and_tax + tip)/100:.2f}")
