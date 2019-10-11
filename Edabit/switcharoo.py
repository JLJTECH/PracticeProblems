#!/usr/bin/env python3
'''
Create a function that takes a string and returns a new string with its first and last characters swapped, except under three conditions.
'''
def flip_end_chars(txt):
    if len(list(txt)) < 2:
        return ('Incompatible.')
    elif isinstance(txt, str) == False:
        return ('Incompatible.')
    elif list(txt)[-1] == list(txt)[0]:
        return ("Two's a pair.")
    else:
        return (list(txt)[-1] + ''.join(list(txt)[1:-1]) + list(txt)[0])

#Alternative Solutions
def flip_end_chars(txt):
	if len(txt) < 2 or not isinstance(txt, str):
		return 'Incompatible.'
	elif txt[0] == txt[-1]:
		return "Two's a pair."
	return txt[-1] + txt[1:-1] + txt[0]
