#!/usr/bin/env python3
'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
'''
def bitter(n):
    b = bin(n).replace("0b","")
    c = b.count("1")

    print(c)

bitter(1234)

#Alternative Solution
return bin(n).count("1")
