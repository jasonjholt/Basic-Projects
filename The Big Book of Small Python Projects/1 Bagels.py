from random import randint

def hints(inp, expect):
    """ checks your input against the expected number """
    clues = []
    
    in_list = [digit for digit in inp]
    check_list = [digit for digit in str(expect)]
    print(in_list, "|", check_list)
    for num in range(len(in_list)):
        if in_list[num] == check_list[num]:
            # digit is in the right place
            clues.append("Fermi")
        elif in_list[num] in check_list:
			# digit in the wrong place
            clues.append("Pico")
    if len(clues) == 0: clues.append("Bagels") # no correct digits
    return (" ".join(clues))
            

def num(n=3):
    """ generates the random number """
    return ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])

print("Let's Play Bagels!")
print("I've got a three digit number in mind! Think you can guess it in 10 tries?")

expected = num()
print(expected)
tries = 0

while tries < 11:
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
