#!/usr/bin/env python3
'''
Create a function that takes a list of positive and negative numbers. 
Return a list where the first element is the count of positive numbers 
and the second element is the sum of negative numbers.
'''
def sum_neg(lst):

    if len(lst) > 0:
        return [len([i for i in lst if i > 0]), sum([i for i in lst if i < 0])]
    else:
        return lst

#Alternative Solutions
def sum_neg(nums):
    if not nums: return []
    return [len([n for n in nums if n > 0]), sum(n for n in nums if n < 0)]

def sum_neg(lst):
  return lst and [sum(1 for x in lst if x>0), sum(x for x in lst if x<0)]
