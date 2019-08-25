#!/usr/bin/env python3
'''
Create a function that takes in a list and returns a list of the accumulating sum.
'''
def accumulating_list(lst):
    nl = []
    cumsum = 0
    for elt in lst:
        cumsum += elt
        nl.append(cumsum)
    return nl

#Alternative solutions
return [sum(lst[:i+1]) for i in range(len(lst))]
