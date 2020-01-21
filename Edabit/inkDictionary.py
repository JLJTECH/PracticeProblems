#!/usr/bin/env python3
'''
Given a dictionary of how many more pages each ink color can print, output the maximum 
number of pages the printer can print before any of the colors run out.
'''
def ink_levels(inks):
    return min([i for i in inks.values()])
    
#Alternative Solutions
def ink_levels(inks):
    return min(inks.values())
