#!/usr/bin/env python3
'''
Given two strings, create a function that returns the total number of unique characters from the combined string.
'''
def count_unique(s1, s2):
  return len(set(s1 + s2))
