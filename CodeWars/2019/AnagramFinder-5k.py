#!/usr/bin/env python3
'''
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none. 
'''
def anagrams(word, words):
    analis = []
    for item in words:
        if (sorted(word) == sorted(item)):
            analis.append(item)
    return analis

#Alternative implementations
def anagrams(word, words): 
  return [item for item in words if sorted(item)==sorted(word)]

def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)
