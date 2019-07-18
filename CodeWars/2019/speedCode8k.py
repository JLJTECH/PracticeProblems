'''Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each 
element in a is strictly greater than the sum of the cubes of each element in b.'''
def array_madness(a,b):
    #Sum the squares in a and evaluate the sum of the cubes in b against a.
    return sum(x ** 2 for x in a) > sum(x **3 for x in b)
