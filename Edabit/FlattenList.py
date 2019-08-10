#!/usr/bin/env python3
'''
Create a function that concatenates n input lists, where n is variable.
'''
def concat(*args):	
	flat_list = [item for sublist in args for item in sublist]
	return flat_list
