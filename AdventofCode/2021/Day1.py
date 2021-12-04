#!/usr/bin/env python3

def solve():
    with open('input.txt') as file:
        #read the full file into object
        content = file.read()
        #split on the new lines and create list
        lcontent = content.split("\n")
        #start counter at 1 to account for first instance
        counter = 1
        for i in range(1, len(lcontent)):
            if lcontent[i] > lcontent[i-1]:
                counter += 1
        print(counter)
solve()
