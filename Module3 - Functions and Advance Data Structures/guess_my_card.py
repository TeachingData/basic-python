# This is extra from the course. As the algo we used was not even near optimized
# The better method is to shrink a set as we eliminate possibilities

from random import sample

# Again if this was bigger I'd use a named tuple or Class but for what we are using
suits = {"hearts", "spades", "clubs", "diamonds"}
values = {'1','2','3','4','5','6','7','8','9','10',"joker","queen","king","Ace"}

# original got a card using random values but we just want a random value (not index) so use sample silly
print(f"Your card is {sample(values,1)[0]} of {sample(suits,1)[0]}")

# We will keep the check for suit (its so small) 
#...but its better to remove options and only use possible valid options
suit = sample(suits, 1)[0]
used = {suit}

# Checks each suit so we only have to ask it 4 times
# (small improvements still possible but leave that as exercise)
while True:
  if input(f"Is {suit} your suit? ")[0] in {'y', 'Y'}:
    break

  if len(used) >= 4:
    # all suits guessed so player is lying
    print("You must have pulled the joker!")
    exit(0)

  while True:
      # have to loop because sample may already be in used
      # this is in-effective, brute-force but sssooo small its not an issue
      suit = sample(suits, 1)[0]
      if suit not in used:
        used.add(suit)
        break

# Now we have the suit but our old algorithm was just okay
# It broke it into chunks so we were not checking every value
# Better is to eliminate possible values and shrink our set
while True:
  if len(values) < 1:
    # Attempted all 14 values so player is lying
    print("You must have the joker!")
    exit(0)

  # We can make this faster by adding a condition (lower or higher)
  # Note: Python greater than uses lexi order (numbers lower than characters)
  value = sample(values, 1)[0]

  if input(f"Is {value} of {suit} your card? ")[0] in {'y', 'Y'}:
    break
  else:
    high_low = input("Is the value higher or lower? ")

    # we will use a slice to create a mutable reassignment of the set
    # regular for loop can be used but we are removing values so have to adjust
    temp = values.copy()
    for v in temp:
      if high_low[0] in {'h', 'H'}:
        if v.zfill(2) <= value.zfill(2):
          values.remove(v)
      else:
        if v.zfill(2) >= value.zfill(2):
          values.remove(v)

print("\nThanks for playing")
