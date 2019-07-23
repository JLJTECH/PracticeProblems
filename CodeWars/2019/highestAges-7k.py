#!/usr/bin/env python3

'''
Take a list of ages and return the two higest ages.
'''
def two_oldest_ages(ages):
    ages.sort(reverse=True)
    return [ages[1], ages[0]]

#Additional implementations
def two_oldest_ages(ages):
    return sorted(ages)[-2:]
