#Write a function powersOfTwo which will return list of all powers of 2 from 0 to n (where n is an exponent).
def powers_of_two(n):
    return [2**x for x in range(n+1)]