#!/usr/bin/env python3
'''
Write a function that takes a list and returns a new list with unique positive (more than 0) numbers.
'''
def unique_lst(lst):
    coll = []
    for i in lst:
        if i > 0 and i not in coll:
            coll.append(i)
    print(coll)

#Alternative solution
return sorted(set(i for i in lst if i > 0), key=lst.index)
