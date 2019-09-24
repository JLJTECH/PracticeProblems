#!/usr/bin/env python3
'''
Create a function, that takes 3 numbers: a, b, c and returns True if the last digit 
of (the last digit of a * the last digit of b) = the last digit of c.
'''
def last_dig(a, b, c):
	a = list(str(a))
	b = list(str(b))
	c = list(str(c))
	val = list(str(int(a[-1]) * int(b[-1])))
	return int(val[-1]) == int(c[-1])
  
#Alternative Solutions
def last_dig(a, b, c):
  return str(a*b)[-1] == str(c)[-1]
  
def last_dig(a, b, c):
	return ((a % 10) * (b % 10) % 10) == (c % 10)
