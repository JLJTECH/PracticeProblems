#!/usr/bin/env python3
'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
'''
def scramble(s1,s2):
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
    return True
    
#Alternative Solutions
def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))

def scramble(s1, s2):    
return len(Counter(s2)- Counter(s1)) == 0
