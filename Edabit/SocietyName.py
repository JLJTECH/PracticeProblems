#!/usr/bin/env python3
'''
Return the first character of each name, joined and alphabetized.
'''
def society_name(friends):
    return ''.join(sorted([i[0] for i in friends])))
