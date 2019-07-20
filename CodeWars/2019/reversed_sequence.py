#!/usr/bin/env python3
'''
Get the number n (n>0) to return the reversed sequence from n to 1.
'''
def reverse_seq(n):
	return list(reversed(range(1, n + 1)))


#Alternative implementations

def reverseseq(n):
    return list(range(n, 0, -1))
