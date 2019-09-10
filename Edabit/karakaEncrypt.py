#!/usr/bin/env python3
'''
Reverse input, replace vowels, add "aca" to end
'''
def encrypt(word):
	word = word[::-1]
	val =  word.translate(str.maketrans("aeou", "0123"))
	return (val + 'aca')

#ALternative Solutions
def encrypt(word):
	return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'
