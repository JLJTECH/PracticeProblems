#!/bin/python3
#Simple while loop to iterate through multiplication of N by position in count. Terminate after 10.
import sys
N = int(input().strip())
count = 1
while (count < 11):
    print (N, "x", count, "=", (N * count))
    count = count + 1