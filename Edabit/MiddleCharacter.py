#!/usr/bin/env python3
'''
Create a function that takes a string and returns the middle character(s). With conditions.
'''
def get_middle(word):
	if len(word) <= 2:
		return word
	elif len(word) % 2 == 0:
		return word[(len(word) // 2) - 1] + word[(len(word) // 2)]
	else:
		return word[(len(word) // 2)]
    
  #Alternative Solutions
def get_middle(word):
  return word[(len(word)-1)//2:(len(word)+2)//2]

def get_middle(word):
  while len(word) > 2:
    word = word[1:-1]
  return word
