#Create an acronym from an imput sentance
def to_acronym(input):
    return "".join(i[0].upper() for i in input.split())

#Alternate solution
def to_acronym(input):
	return ''.join(word[0] for word in input.split()).upper()