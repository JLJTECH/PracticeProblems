#!/usr/bin/env python3

'''
Recieve a message and you will need to get the frequency of each and every character
'''

def char_freq(message):
    return {i : message.count(i) for i in set(message)} 

char_freq("I like cats")
