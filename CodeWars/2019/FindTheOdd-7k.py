#!/usr/bin/env python3
'''
Given an array, find the int that appears an odd number of times.
'''
def find_it(seq):
    cnt = 0
    for i in seq:
        cnt = cnt ^ i
    return cnt
 
#Alternative solutions
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
