#!/usr/bin/env python3
'''
Are these smooth sentences? A smooth sentence is one where the last letter of each word is identical to the first letter the following word.
'''
def is_smooth(sentence):
    sl = sentence.split()
    first = [i[0] for i in sl]
    last = [i[-1] for i in sl]
    return first[1:] == last[:-1]
