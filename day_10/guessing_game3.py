#!/usr/bin/env python3

"""
Author: HealthTechKid
Date: 24 / 05 / 2024
Purpose: Purpose: The program randomly selects a number between 0 and 10
7 and stores it in the variable `secret` without displaying it to the user.
It then prompts the user to guess the selected number. If the user
guesses correctly, the program displays 'You won!'. If the guess is incorrect,
it displays 'You lost! The correct number was ' followed by the value of `secret`.
"""

import random

# Generate the secret number
secret = random.randint(0, 10)

print("This is a guessing game. Please guess a number between 0 and 10.")

# Number of attempts
attempts = 3

for attempt in range(attempts):
    guess = int(input("Put your number here: "))
    if guess == secret:
        print("YOU WON!!! 🎉")
        break
    else:
        if attempt < attempts - 1:
            print(f"You lost, but you have {attempts - attempt - 1} attempt(s) left. Try again.")
        else:
            print(f"YOU LOST, GAME OVER. The correct number was {secret}.")
