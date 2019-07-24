#!/usr/bin/env python3

'''
Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
'''

def correct(string):
    d = {"5" : "S", "0" : "O", "1" : "I"}
    replaced = ''.join(d.get(char, char) for char in string)
    
    return replaced

#Alternative Implementations
def correct(string):
    return string.translate(str.maketrans("501", "SOI"))


def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')
