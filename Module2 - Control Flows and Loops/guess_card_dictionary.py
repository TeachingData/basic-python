"""We'll use this to first - create a dictionary for our player with name, a nickname, # of guesses to true, and currentcard
Then we'll add code for building a deck of cards (using a dictionary - I'd usually use a set) as and an example with functions for setting the card
"""

from random import sample, randrange


def get_card() -> list:
    # Build our card as a suit and value
    suits = {"hearts", "spades", "clubs", "diamonds"}
    return [sample(suits, 1)[0], randrange(1,14)]


def get_playername() -> str:
    return input("Please enter your name: ")


def get_nickname(flag='n') -> str:
    if flag.upper().startswith("N"):
        return ""
    return input("Please enter your nickname: ")

# standard deck of cards
deck = {"hearts": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Joker', 'Queen', 'King', 'Ace'],
        "spades": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Joker', 'Queen', 'King', 'Ace'],
        "clubs": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Joker', 'Queen', 'King', 'Ace'],
        "diamonds": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Joker', 'Queen', 'King', 'Ace']
        }

# player
player = {"name": "",
          "nickname": "",
          "numguesses": [],
          "currentsuit": "",
          "currentvalue": ""
          }

# tracker for current guesses
guesses = 0

# assign player suit and value
player["currentsuit"], player["currentvalue"] = get_card()
player["name"] = get_playername()

nickflag = input("Do you have a nickname (y/n)? ")
player["nickname"] = get_nickname(nickflag)
print(f"Your card is {player['currentvalue']} of {player['currentsuit']}")

used = set()
while True:
    suit = sample(deck.keys(), 1)[0]
    if suit not in used:
        used.add(suit)
        guesses += 1

        if input(f"Is {suit} your suit? ").lower().startswith('y') or len(used) >= 4:
            break

print(f"suit guessing took {guesses} and its suit {suit}")

used = set()
while True:
    value = sample(deck[suit], 1)[0]
    if value not in used:
        used.add(value)
        guesses += 1

        if input(f"Is {value} of {suit} your card? ").lower().startswith('y'):
            break
        else:
            high_low = input("Is the value higher or lower (h/l)? ")

            for v in deck[suit]:
                # so we walk through the suit and add everything lower/higher to used so it won't be tried again
                if high_low.lower().startswith('h'):
                    if v.zfill(2) < value.zfill(2):
                        used.add(v)
                else:
                    if v.zfill(2) > value.zfill(2):
                        used.add(v)


print(f"\nThanks for playing! - it took {guesses} guesses")
