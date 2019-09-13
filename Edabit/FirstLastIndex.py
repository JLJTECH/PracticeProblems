#!/usr/bin/env python3
'''
Given a word, write a function that returns the first index and the last index of a character.
'''
def char_index(word, char):
    return None if char not in word else [word.index(char), word.rindex(char)]
