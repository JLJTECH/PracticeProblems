#!/usr/bin/env python3
'''
Take the string inputs and combine the letters in sequence.
'''

def triple_trouble(one, two, three):
    #Empty string to collect values
    collector = ""
    
    #Start counter
    size = 0
    
    #Check size and compare against fixed length of variables
    while size < len(one):
    
        #Format output and append to collector
        collector += one[size]+two[size]+three[size]
        
        #Increment the counter by one
        size += 1
    
    return collector
