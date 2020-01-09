#!/usr/bin/env python3
'''
Create a function that takes two numbers as arguments (num, length) and returns a list of multiples
'''
def list_of_multiples (num, length):

    coll = []
    while length > 0:
        coll.append(num * length)
        length -= 1
        pass
    return coll[::-1]

#Alternative solutions
def list_of_multiples (num, length):
    return [i*num for i in range(1,length+1)]
