#!/usr/bin/env python3

'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
'''
def fake_bin(x):
    return ''.join(['0' if int(i) < 5 else '1' for i in x])
    
#Additional implementations
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
    
def fake_bin(x):
val = [int(i) for i in x]
    collection = []
    for i in val:
        if i < 5:
            collection += '0' 
        else:
            collection += '1' 
    return ''.join(collection)

