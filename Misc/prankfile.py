#!/usr/bin/env python3

import os
import time
import sys

def hello():

    #Get count of repetition
    n = int(input("How many? "))

    while n > 0:
        os.system('say thank you')
        time.sleep(0.25)
        n -= 1

    #Multi line comment for large ascii
    print(""" HOWDY, THIS IS A MULTI LINE """)

    #Output character by character with .25 second delay
    string = "Hello"
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.25)
           
hello()
