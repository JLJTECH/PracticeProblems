#Return array in same order with duplicates removed.
def unique(integers):
    unique = []
    [unique.append(item) for item in integers if item not in unique]
    return unique


#Alternate Solution
def unique(integers):
    l = []
    for i in integers:
        if not i in l: l.append(i)
    return l