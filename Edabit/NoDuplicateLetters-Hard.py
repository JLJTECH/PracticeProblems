#!/usr/bin/env python3
'''
Given a common phrase, return False if any individual word in the phrase contains duplicate letters. 
Return True otherwise.
'''
def no_duplicate_letters(phrase):
	val = [phrase]
	nlst = ' '.join(val).split()
	st = [len(i) for i in nlst]
	ev = [len(set(i)) for i in nlst]

	return st == ev

#Alternative solutions
def no_duplicate_letters(phrase):
  return all(i.count(j)==1 for i in phrase.split() for j in i)

def no_duplicate_letters(phrase):
	return all([len(set(i))==len(i) for i in phrase.split(' ')])
