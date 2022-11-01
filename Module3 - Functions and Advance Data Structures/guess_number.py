# Simple number guessing game to show state machine, spin lock, and event based programming
import random

# global constant of possible states and return values
states = { 
        "win": "This is correct! You win!",
        "end": "Thanks for playing. Bye!",
        "lower": "The correct number is lower",
        "higher": "The correct number is higher"
        }


def init():
    """
    Initialize game, and generates a random int (1 - 10)
    And prints our intro screen

    returns:
      * gamestate - None object as we just started
      * correct number - random number 1 to 10
    """
    print("Welcome Player! Please guess numbers between 1 and 10!")
    return "", random.randint(1,10)


def getguess():
    """
    Get's player's guess

    Output:
      * playerNumber: the number entered by the player, or None if the player wants to stop the game
    """

    while True:
        # Player input
        word = input("What is the correct number? Enter to 'quit' to quit: ")
        # Quit if the player types "quit"
        if word.lower() == "quit":
            return None
            # if returns None we can assign and check for then exit as end state

        # Int casting with exception handling
        try:
            guess = int(word)
            break
        except ValueError:
            print("Please type a number without decimals!")
            continue

    return guess 


def update(gamestate,correctnum,guess):
    """
    Update game state: this is a very simple finite state machine
    more a rule based thing

    parameters:
      * gamestate: the state of the game
      * correctnum: the magic number to find
      * guess: player's guess
    return:
      * gamestate: the state
    """
    if guess is None:
        gamestate = "end"
    elif guess == correctnum:
        gamestate = "win"
    elif correctnum < guess:
        gamestate = "lower"
    elif correctnum > guess:
        gamestate = "higher"

    return gamestate


def render(gamestate):
    """
    Render game state

    Parameters:
      * gamestate: the current state of the game, "win", "end", "lower" or "higher"
    """
    global states

    # Cases (switch statement Python style)
    if gamestate in states:
        print(states[gamestate])
    else:
        raise RuntimeError("Unexpected state {}".format(gamestate))


def runGame():
# Our very simple game loop
    gamestate, correctnum = init()
    while gamestate != "win" and gamestate != "end":
        guess = getguess()
        gamestate = update(gamestate,correctnum,guess)
        render(gamestate)


# Launch the game
runGame()
