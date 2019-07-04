#!/usr/bin/env python3
'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot seperating them.
'''

def abbrevName(name):
    hold = name.split()
    firword = list(hold[0])
    secword = list(hold[1])
    return firword[0].upper() + "." + secword[0].upper()
    
 #Streamline
 return '.'.join(w[0] for w in name.split()).upper()
 
 first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
