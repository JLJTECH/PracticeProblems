#!/usr/bin/env python3
'''
Generate formatted hex color values from RGB input.
'''
def hexcol(a,b,c):
	x = hex(a)
	y = hex(b)
	z = hex(c)
	
	print("#" + (str(x[2:]).rjust(2,'0') + str(y[2:]).rjust(2,'0') + str(z[2:]).rjust(2,'0')).upper())
	
  #For splitting outputs in debug
  print("----" * 20)

#Test Outputs
hexcol(255, 99, 71)
hexcol(255, 99, 71)
hexcol(184, 134, 11)
hexcol(189, 183, 107) 
hexcol(0, 0, 205)
