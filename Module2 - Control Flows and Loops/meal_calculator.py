# This was used to teach looping, type conversion, and lists in Python
# few "constants"
TAXRATE = .065
TIPRATE = .18

# list for transaction costs & total variable
# we are going to use ints for our prices because its better
prices = []
total = 0

# we can loop over the actual input or until we decide to exit
# I prefer True with break (because of a bit better logic) both work
while True:
    if input("Please select from the following:\n0: <add> an item\n1: <done>\n[ ]\b\b") == "0":
        # Get item price, check if >0 and convert to int: add to list
        item_price = input("What was the price of the item? $")
        if item_price > "0":
            item_price = int(float(item_price) * 100)
            prices.append(item_price)
            total += item_price
        else:
            print("Price must be greater than 0")
    else:
        break
        
# check if client added any prices and exit if they didn't
if not prices:
    print("Sorry you couldn't find any item you liked but thanks for coming!")
    quit()

# Print out each item and sumation of all; calculate tax and print out
# for or foreach loop: for (c-style) loops over each index (using range or *enumerate*)
# foreach: loops over iterable and returns the value
for price in prices:
    print(f"The price of the item is {price/100:.2f} with tax of {TAXRATE * price/100:.2f}")

# print out total taxes and price then ask for tip and add
tax = total * TAXRATE
print(f"The total is {total/100:.2f} with taxes of {tax/100:.2f} for a total of {total/100 + tax/100:.2f}")

tip = input(f"Your suggested tip is {total * TIPRATE/100:.2f}\nPlease enter your tip: $")
if tip < "0":
    tip = 0
tip = int(float(tip) * 100)
print(f"With tip of {tip/100:.2f} your total is {total/100 + tax/100 + tip/100:.2f}")
