#!/usr/bin/env python3
'''
Create a function that takes a list of 10 numbers (between 0 and 9) 
and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).
'''
def format_phone_number(lst):
    val = ''.join([str(i) for i in lst])
    return ("(" + val[:3] + ")" + " " + val[3:6] + "-" + val[6:])

#Alternative Solutions
def format_phone_number(lst):
  return '({}{}{}) {}{}{}-{}{}{}{}'.format(*lst)
