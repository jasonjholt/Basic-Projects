""" 
converts numerical input into binary
"""

while True:
    c = (input("Number: ")).lower()
    if c == "done":
        print("Done!")
        break
    try:
        n = int(c)
    except ValueError:
        print("Not a number!")
        break
    st = ""

    while n//2 != 0:
        st += str(n%2)
        n = n//2
    st += str(n%2)
    
    print(st[::-1])
