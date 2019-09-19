#!/usr/bin/env python3
'''
Write a function that counts the number of times a specific digit occurs in a range (inclusive).
'''
def digit_occurrences(start, end, digit):
    val = [int(i) for i in range(start, end+1)]
    brk = ''.join(map(str, val))
    return brk.count(str(digit))

#What I should have written
    val = ''.join(str(i) for i in range(start,end+1))
    return val.count(str(digit))
