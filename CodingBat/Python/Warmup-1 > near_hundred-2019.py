#!/usr/bin/python3
'''
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
'''
def near_hundred(n):
  #return abs(n) in range(89, 111) or range(189, 211)
  if n in range(90, 111):
    return True
  elif n in range(190, 211):
    return True
  else:
    return False

 #Additional implementation
 def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
