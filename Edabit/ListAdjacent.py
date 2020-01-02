#!/usr/bin/env python3
'''
Sam and Frodo need to be close. 
If they are side by side in the list, your function should return True. 
If there is a name between them, return False.
'''
def middle_earth(lst):
    s = lst.index('Sam')
    f = lst.index('Frodo')
    if s + 1 == f or s - 1 == f:
        return True
    else:
        return False

#Alternative Solutions
def middle_earth(lst):
    return abs(lst.index('Sam') - lst.index('Frodo')) == 1
