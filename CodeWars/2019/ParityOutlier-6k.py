#!/usr/bin/env python3
'''
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.
'''
def find_outlier(integers):
    odd = [num for num in integers if num % 2 == 1]
    even = [num for num in integers if num % 2 == 0]
    
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]

#Alternative solutions
return odds[0] if len(odds)<len(evens) else evens[0]

parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
