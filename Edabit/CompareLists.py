#!/usr/bin/env python3
'''
Create a function that takes in two lists: the list of user-typed words, and the list 
of correctly-typed words and outputs a list containing 1s (correctly-typed words) and -1s (incorrectly-typed words).
'''
def correct_stream(user, correct):
	return [1 if user[i] == correct[i] else -1 for i in range(len(user))]
