#!/usr/bin/env python3
'''
Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
'''
def sum_two_smallest_nums(lst):
	nlst = [i for i in lst if i > 0]
	return sorted(nlst)[0] + sorted(nlst)[1]

#Alternative solutions
def sum_two_smallest_nums(lst):
	return sum(sorted([x for x in lst if x > 0])[:2])
