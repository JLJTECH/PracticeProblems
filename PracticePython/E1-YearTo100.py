#!/usr/bin/env python3
'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
def namer(name, age):
	name  = input("What is your name? ")
	age = input("How old are you? ")
	tocent = 100 - int(age)
	centyr = 2019 + int(tocent)
	print("Your name is " + name + ". You are " + age + " and will be 100 in " + str(tocent) + " years! That's in the year " + str(centyr) + "!")

namer("a", 22)
