#!/usr/bin/env python3
'''
Create a function that takes a string and returns True if the sum of index 
(position) on every letters in word (in English alphabet) is even or return False if the sum is odd
'''
def in_alpha(word):
    chars = [i for i in word]
    clean = ''.join(e for e in chars if e.isalnum())
    aval = sum([ord(i) - 96 for i in clean])
    return aval % 2 == 0

#Alternative Solutions
def inalpha(word):
    return sum(ord(i) - 96 for i in word if i.isalpha())%2 == 0
