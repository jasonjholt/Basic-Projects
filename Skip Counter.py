"""
basic skip counting program
inputs an ending number and a number to count by
checks for invalid inputs and quits program if input is invalid
"""

import math

skip_count = []

print("Let's skip count!")
try:
    s = int(input("What number should we count by? "))
    f = 1 + int(input("Where should we end? "))
except:
    print("Invalid Data")
    quit()
    
for n in range (s,f):
    if n%s == 0:
        skip_count.append(n)


print("Your list is: ")
print(skip_count)

print(" ")
print("I have counted " + str(len(skip_count)) + " multiples in our range")
