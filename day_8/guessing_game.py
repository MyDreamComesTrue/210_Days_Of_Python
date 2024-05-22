#!/usr/bin/env python3

"""
Author: HealthTechKid
Date: 22 / 05 / 2024
Purpose: The program randomly selects a number between 0 and 10 
and stores it in the variable `secret` without displaying it to the user.
It then prompts the user to guess the selected number. If the user 
guesses correctly, the program displays 'You won!'. If the guess is incorrect,
it displays 'You lost! The correct number was ' followed by the value of `secret`.
"""

import random
secret = random.randint(0, 10)
print("This is a guessing game. Please guess a number between 0 to 10.")
x = int(input("Put your number here: "))
if x == secret:
	print("You won!")
else:
	print("You lost! The correct number is:", secret)
