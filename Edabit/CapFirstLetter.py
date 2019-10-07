#!/usr/bin/env python3
'''
Create a function that takes a string as an argument and converts the first character of each word to uppercase. 
Return the newly formatted string.
'''
def make_title(txt):
    lst = [word[0].upper() + word[1:] for word in txt.split()]
    s = " ".join(lst)
    return s

#Alternative Solutions
def make_title(txt):
  return ' '.join([i.capitalize() for i in txt.split(' ')])
