#CodeFights Intro Gates
#Add Two Digits
#You are given a two-digit integer n. Return the sum of its digits.

def addTwoDigits(n):
    	return sum(int(i) for i in str(n))
