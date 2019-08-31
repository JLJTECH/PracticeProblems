#!/usr/bin/env python3
'''
Each lowercase letter becomes uppercase and each uppercase letter becomes lowercase
'''
def to_alternating_case(string):
    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)
    
#Alternative solutions
def to_alternating_case(string):
    return string.swapcase()
