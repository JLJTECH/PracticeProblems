#!/usr/bin/env python3
'''
Example of using Maketrans to translate and replace multiple letters in a string. 
'''

from string import maketrans

def tran(dna):
	inv = "ATGC"
	outv = "TACG"
	trantab = maketrans(inv, outv)
	print(dna.translate(trantab))

tran("GTAT")
