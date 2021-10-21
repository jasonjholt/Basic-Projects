""" basic rock paper scissors against the computer

print out player and computer choice
print result of game
keeps going until player says 'done'
"""

import random

print("Tell me when you're ready to quit by saying 'done'!")

while True:
    list = ["rock","paper","scissors"]
    c = random.choice(list)
    p1 = str((input("Rock, Paper, or Scissors? "))).lower()
    # print(c)

    if p1 == "done":
        print("Nice playing with you!")
        break

    print(f"\nYou chose {p1}, I choose {c}!")

    if c == p1:
        print(f"We both chose {p1}. It's a tie!")
    elif p1 == "rock":
        if c == "scissors":
            print("You have won! Congratulations!")
        else:
            print("Better luck next time!")
    elif p1 == "scissors":
        if c == "paper":
            print("You have won! Congratulations!")
        else:
            print("Better luck next time!")
    elif p1 == "paper":
        if c == "rock":
            print("You have won! Congratulations!")
        else:
            print("Better luck next time!")
    else:
        print("Huh? I don't know what that is.")
