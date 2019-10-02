#!/usr/bin/env python3
'''
Return True if every even index contains an even number and every odd index contains an odd number. Else return False 
'''
def is_special_array(lst):
	a = [i for i in lst[::2] if i % 2 == 1]
	b = [i for i in lst[1::2] if i % 2 == 0]
	return len(a) == len(b)

#Alternative Solutions
def is_special_array(lst):
	return all(lst[i]%2==i%2 for i in range(len(lst)))
  
