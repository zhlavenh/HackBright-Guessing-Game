"""A number-guessing game."""
import random  # java.until.Random for Java

# greet player
print("Welcome it the Guessing Game!")

# get player name
userName = input("What is your name?")  # stores name into variable
print(f"{userName} I'm thinking of a number between 1 and 100")
print("Try to guess my number. ")  # System.out.printin for java


# choose random number between 1 and 100
# computer = random.randint(1, 100)  # rand = new Random() for Java
computer = 68


counter = 0
guessed = False  # Setting guessed to False
validEntry = False

# Game loop
# Elif = else if Java
# repeat forever
while not guessed:  # loop intil user guesses correct number
    counter += 1
    # Get Guess
    UserGuess = int(input("Your Guess? "))  # prompt user for guess
    if UserGuess < 1 and UserGuess > 100:
        print("Please enter a valid number?")
    # if incorrect give hint and increase guesses
    if UserGuess < computer:  # if guess is too l
        print("Guess is too low, try again.")

    elif UserGuess > computer:  # If guess is too high
        print("Your guess is too high, try again.")

    # congradulate player
    elif UserGuess == computer:  # if guess is correct
        print(
            f"Well done, {userName}!. You found my number in {str(counter)} tries!")
        guessed = True  # Set guessed to true to stop loop
