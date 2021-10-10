#!/bin/env python3

#Check string for negative number. If any other alpha values in string, return false.

def isDigit(string):
    return string.lstrip('-').replace('.','').isdigit()
 
test.assert_equals(isDigit("s2324"), False)
test.assert_equals(isDigit("-234.4"), True)
test.assert_equals(isDigit("3 4"), False)
test.assert_equals(isDigit("3-4"), False)
test.assert_equals(isDigit("3 4   "), False)
test.assert_equals(isDigit("34.65"), True)
test.assert_equals(isDigit("-0"), True)
test.assert_equals(isDigit("0.0"), True)
test.assert_equals(isDigit(""), False)
test.assert_equals(isDigit(" "), False)
