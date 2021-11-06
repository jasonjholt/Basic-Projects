""" 
user has to guess a random 3 digit number
per digit, if a digit is in the right place, the hint is fermi. if its in the wrong place, pico
if the digit is not in the expected number, hint is bagels
10 maximum tries, print a new value everytime an attempt is made

if user is unable to guess, print the expected number
"""


from random import randint

def hints(inp, expect):
    """ checks your input against the expected number """
    clues = []
    
    in_list = [digit for digit in inp]
    check_list = [digit for digit in str(expect)]
    for num in range(len(in_list)):
        if in_list[num] == check_list[num]:
            clues.append("Fermi")
        elif in_list[num] in check_list:
            clues.append("Pico")
    if len(clues) == 0: clues.append("Bagels")
    return (" ".join(clues))
            

def num(n=3):
    """ generates the random number """
    return ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])

print("Let's Play Bagels!")
print("I've got a three digit number in mind! Think you can guess it in 10 tries?")

expected = num()
tries = 0

while tries < 10:
    print(10 - tries, "tries left!")
    inp = input(">>>")
    if inp == "done": break
    # . . . 
    if inp == expected:
        print("You got it!")
        break
    else:
        print(hints(inp, expected))
        tries += 1

if tries == 10:
    print(f"Aww, too bad. The number was {expected}.")
else:
    print(f"Congratulations! The number is {expected}.")
