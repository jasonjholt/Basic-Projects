import math

primes = []

print("I will generate a list of primes from an initial number to a final number.")
s = int(input("Initial Number: "))
f = 1 + int(input("Final Number: "))

if s >= f:
    print("Oops! Your initial number is larger than your final number!")
    print(". . .")
    exit()
elif s == f - 1:
    print("Oops! Your numbers are equal!")
    print(". . .")
    exit()
    
for n in range (s,f):
    for x in range(2,n):
        if n % x == 0:
            break
    else:
        primes.append(n)

len(primes)

print(primes)
print("There are " + str(len(primes)) + " prime numbers in that range.")
