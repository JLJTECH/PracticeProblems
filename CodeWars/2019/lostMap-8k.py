#!/usr/bin/env python3
'''
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''
def maps(a):
    pass
    result = map(lambda x: x + x, a)
    return list(result)
 
 #Additional implementations:
 def maps(a):
    return [2 * x for x in a]
    
  def maps(a):
    return map(lambda x:2*x, a)
