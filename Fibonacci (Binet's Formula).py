import math

def fibb(n):
    """ f_n = F_n-1 + F_n-2
    returns a list until the nth term of the fibonacci sequence
    """
    f = []
    p = 0
    while p < n:
        g1 = (1 + math.sqrt(5))/2
        g2 = (1 - math.sqrt(5))/2
        f.append(int(((g1**p) - (g2**p)) / math.sqrt(5)))
        p += 1
    return f
