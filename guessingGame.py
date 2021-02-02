# Import the random module for generating random numbers
import random

# Message to start game & instructions
print("\nA number between 1 and 9 has been generated!\nYou have only 5 chances to guess the number!\nStart Guessing!\n")

# Initializing variables
number = random.randint(1, 9)
guessCount = 0

# The condition
while guessCount < 5:
    guess = int(input("Enter your guess: "))
    guessCount += 1
    if number > guess:
        print("\nYour guess is smaller than the number, try guessing higher!\n")
    elif number < guess:
        print("\nYour guess is higher than the number, try guessing smaller!\n")
    if number == guess:
        print("\nYaY! You did it in " + str(guessCount) + " try(s)\n")
        break

if guess == number:
    print("You guessed the number in " + str(guessCount) + " try(s)!")
else:
    print("Your 5 tries are over! You could'nt guess the number\nThe number was " + str(number))