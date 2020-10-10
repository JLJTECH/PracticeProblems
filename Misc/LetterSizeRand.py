#!/usr/bin/env python3

'''
Letter Randomization for fun
'''

import random

def rando():
    sen = "This is the stuff for randomization."
    lst = [str.upper, str.lower]
    print(''.join([random.choice(lst)(i)for i in sen]))

rando()
