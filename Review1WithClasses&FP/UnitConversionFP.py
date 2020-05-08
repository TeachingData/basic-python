import re
""" This looks at a Functional Programming(-ish) way of performing our conversions
    ....Not gonna lie - I wouldn't use this version for this (its more useful as a library)
    However: I do use a version like this when I have more dynamic or statistical based calcs
        so this is a good way to introduce the technique and look at regex in Python
    This is called a "dictionary of partials" and can also use named (defined) functions
"""

CONVERT = {
    "feet": lambda num: num / 12,
    "yards": lambda num: num / 36,
    "miles": lambda num: num / 63360,
    "centimeters": lambda num: num / 2.54
}

# We are using FP so.....I might as use a regex too (to capture any single/multi-digit numbers)
# If you don't get it at this point - don't worry - just use the version from 1st iteration
user_info = re.findall(r'[0-9]+',
            input("Please enter the number of feet and inches (as [0+] ft [0+] inches)"))

#user_info will be a list of all matches so (yes you could make this a while loop - leave that to you):
try:
    user_inches = float(user_info[0]) * 12 + float(user_info[1])
except (ValueError, IndexError):
    print("You must enter two numeric values for feet & inches")
    user_inches = 0.0

print(f'You have {user_inches} inches')
for unit in CONVERT.keys():
    print(f'You have {CONVERT[unit](user_inches):.4f} {unit}')

