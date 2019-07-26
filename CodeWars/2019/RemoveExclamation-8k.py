#!/usr/bin/env python3
'''
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
'''
def remove_exclamation_marks(s):
    bad = ["!"]
    s = ''.join(i for i in s if not i in bad)
    return s

#Alternative implementations
def remove_exclamation_marks(s):
    return s.replace('!', '')
