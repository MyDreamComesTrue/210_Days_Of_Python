#!/usr/bin/env python3

"""
Author: HealthTechKid
Date: 25 / 05 / 2024
Purpose: The program randomly selects a number between 0 and 100
and stores it in the variable `secret` without displaying it to the user.
It then prompts the user to guess the selected number. If the user
guesses correctly, the program displays 'You won!'. If the guess is incorrect,
it displays 'You lost! The correct number was ' followed by the value of `secret`.
"""

import random
guess = random.randint(0, 100)

attempts = 6

for attempt in range(attempts):
    x = int(input("Please enter your number here: "))
    if x == guess and x <= 100:
        print("Congratulations, you WON !!!\n"
              f"You guessed it in {attempt + 1} attempt(s).")
        break
    elif x < guess and x <= 100:
        print("Too small")
    elif x > guess and x <= 100:
        print("Too big")
else:
    print("YOU LOST ! After 6 attempts.\n"
          f"The secret number is {guess}.\n"
          "Don't be discouraged. Please try again. Many people succeed after several rounds.")
