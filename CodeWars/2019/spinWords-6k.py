#!/usr/bin/env python3
'''
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed
'''
def spin_words(sentence):
    words = sentence.split(" ")
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in words])

#Alternate solutions
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
