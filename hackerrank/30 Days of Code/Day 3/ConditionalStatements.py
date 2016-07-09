#!/bin/python

import sys
N = int(raw_input().strip())
if N % 2 == 0 and (N < 6 or N > 20):
    print "Not",
print "Weird";
