""" rolls as many die as the user gives

program terminates when input has characters other than digits
"""

import random

def roll(die):
    rolls = []
    for dice in range(die):
        num = random.randint(1,6)
        rolls.append(num)
    print(rolls)

while True:
    dices = input("How many die do you have? ")
    try:
        d = int(dices)
    except ValueError: # predicting text inputs # can be done with isdigit()
        print("Done!")
        break
    
    roll(d)
