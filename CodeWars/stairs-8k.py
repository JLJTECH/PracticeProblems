#!/usr/bin/env python3

'''
Use the map function to iterate through the nested array and sum all values. Then multipy the sum by 20 to get the 20 year estimate.
'''

def stairs_in_20(stairs):
    val = sum(map(sum, stairs))
    return val * 20
