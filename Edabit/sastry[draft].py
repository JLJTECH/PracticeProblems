#This will be finished once i'm awake. This is but a placeholder while I work.

import math

def sass(n):
    v = str(n - 1)
    c = str(n)

    forward = int(v + c)

    while forward > 0:
        print(forward)
        print(math.sqrt(forward))
        print("* * * " * 5 )
        forward -= 1


sass(110)
