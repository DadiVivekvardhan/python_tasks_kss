#Q. Create a Number Guessing Game where:
#● The program generates a random number between 1 and 50 using random.
#● The user has 5 attempts to guess the number.
#After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number.


import random
import math

number = random.randint(1, 50)

for i in range(1, 6):
    guess = int(input(f"Attempt {i}/5 - Enter your guess (1-50): "))

    difference = math.fabs(number - guess)

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low!")
        print("You are", difference, "away from the correct number.")
    else:
        print("Too high!")
        print("You are", difference, "away from the correct number.")

if guess != number:
    print("Sorry! You have used all 5 attempts.")
    print("The correct number was:", number)
