n = int(raw_input())
l = len(format(n,'b'))
for x in range(1, n+1):
	print str(x).rjust(l), format(x, 'o').rjust(l), format(x, 'x').rjust(l).upper(), format(x, 'b').rjust(l)

#Old Submission without left justification.
	for x in range(input()):
    print x + 1, "", int(oct(x + 1)), "", hex(x + 1)[2:], "", bin(x + 1)[2:] 