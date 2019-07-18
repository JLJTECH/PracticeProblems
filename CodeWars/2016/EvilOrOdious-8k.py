def evil(n):
    a = bin(n)[2:]
    b = a.count('1')

    if b % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"