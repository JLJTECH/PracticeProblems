#Return list index of all capital letters in string
def capitals(word):
    return [l for l, c in enumerate(word) if c.isupper()]

#Alternate Solution
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]