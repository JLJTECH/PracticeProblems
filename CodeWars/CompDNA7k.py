#!/usr/bin/env python3
'''
You have a function with one side of the DNA string; you need to get the other complementary side.
DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA"
'''
def DNA_strand(dna):
    d = {"A":"T", "T":"A", "G":"C", "C":"G"}
    replaced = ''.join(d.get(char, char) for char in dna)
    return replaced

#Other methods
