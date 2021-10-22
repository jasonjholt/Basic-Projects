""" basic guessing game with the computer"""

from random import randint

name = input("Hi! What's your name? ")
lim = input("What's the highest possible number you want me to pick from? ")


print(f"Well, {name}, I have picked a number between 1 and {lim}!")
num = randint(1, int(lim))
guesses = 0
max_guess = int(input("How many times do you want to guess? "))

while guesses < max_guess - 1:
    my_guess = int(input("Can you guess it? "))
    print(f"{name}, your guess is {my_guess}.")
    guesses = guesses + 1
    
    if my_guess == num:
        print(f"Congratulations! You guessed the number in {guesses} guesses!")
        break
    elif my_guess <= 0:
        print("That's way too low! I'm leaving!")
        break
    elif my_guess > int(lim):
        print("That's way too high! I'm leaving!")
        break
    elif my_guess < num and my_guess < int(lim) and my_guess > 0:
        print("Your number is too low! Care to try again? ")
    elif my_guess > num and my_guess < int(lim) and my_guess > 0:
        print("Your number is too high! Care to try again? ")

while guesses == max_guess - 1:
    my_guess = int(input("Can you guess it? "))
    print(f"{name}, your guess is {my_guess}.")
    guesses = guesses + 1
    
    if my_guess == num:
        print(f"Congratulations! You guessed the number in {guesses} guesses!")
        break
    elif my_guess <= 0:
        print("That's way too low! I'm leaving!")
        break
    elif my_guess > int(lim):
        print("That's way too high! I'm leaving!")
        break
    elif my_guess < num and my_guess < int(lim) and my_guess > 0:
        print("Your number is too low!")
    elif my_guess > num and my_guess < int(lim) and my_guess > 0:
        print("Your number is too high!")

if my_guess != num and my_guess < int(lim) and my_guess > 0:
    print(f"I'm sorry! My number was {num}.")



