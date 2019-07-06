#!/usr/bin/env python3

'''
count ocurrence of specific letters and put in fraction format over length of input. 
'''

def printer_error(s):
    size = str(len(s))
    tally = 0
    for i in s:
    	if i > "m":
    		tally += 1
    print(str(tally) + "/" + size)
    # use return for solution


#fast implementations
return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
