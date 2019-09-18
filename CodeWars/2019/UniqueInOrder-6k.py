#!/usr/bin/env python3
'''
Return a list of items without any elements with the same value next to each other and preserve the original order of elements.
'''
def unique_in_order(a):
    newlist = []
    for i in a:
        if len(newlist) < 1 or not i == newlist[len(newlist) -1]:
            newlist.append(i)
    return newlist
    
#Alternative Solutions
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
