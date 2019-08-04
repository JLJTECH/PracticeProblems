#!/usr/bin/env python3

'''
Create a function that takes a list of items and checks if the last item matches the rest of the list.
'''
def match_last_item(lst):
	arr = lst[:-1]
	jin = "".join(str(x) for x in arr)
	last = lst[-1]
	if jin.lower() == last.lower():
		return True
	else:
		return False
    
# Alternative Solutions
def match_last_item(lst):
	return ''.join(str(i) for i in lst[:-1]).lower() == lst[-1].lower()
