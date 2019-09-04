#!/usr/bin/env python3
'''
The digit distance between two numbers is the absolute value of the difference of each digit.
Create a function that returns the digit distance between two integers.
'''
def digit_distance(num1, num2):
	val1 = [int(d) for d in str(num1)]
	val2 = [int(d) for d in str(num2)]
	subr = [y - x for x, y in zip(val1, val2)]
	Sum = sum(subr)
	return Sum

#Alternative Solutions
def digit_distance(num1, num2):
	return sum(map(int,str(abs(num1-num2))))
