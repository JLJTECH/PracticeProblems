#Write a function findNeedle() that takes an array full of junk but containing one "needle"
   return "found the needle at position {}".format(haystack.index("needle"))

#Alternate Solution
def find_needle(haystack): 
	return 'found the needle at position %d' % haystack.index('needle')
