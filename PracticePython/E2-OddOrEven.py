#!/usr/bin/env python3
'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
'''

def odev(num, check):
	#ask for number
	num = input("Provide a number: ")
	check = input("Provide a check digit: ")
	#multiple of 4 - different message
	if int(num) % 4 == 0:
		print("Well looks like we have a multiple of 4!")
	#odd or even
	elif int(num) % 2 == 0:
		print("Your number is even.")
	else:
		print("Your number is odd.")
	#num and check - divide evenly by check
	if int(num) % int(check) == 0:
		print("Your number is evenly divisible by the check digit!")
	else:
		print("Try again next time.")

odev(6,1)
