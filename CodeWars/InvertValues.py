#!/usr/bin/env python3
'''
Given a set of numbers, return the additive inverse of each. 
Each positive becomes negative, and the negatives become positive.
'''

def invert(lst):
    return [-i if i else abs(i) for i in lst]
