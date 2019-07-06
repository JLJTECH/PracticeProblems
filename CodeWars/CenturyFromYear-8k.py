#!/usr/bin/env python3
'''
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.
Given a year, return the century it is in.
'''

def century(year):
    
    return (year -1) // 100 + 1

century(1122)
