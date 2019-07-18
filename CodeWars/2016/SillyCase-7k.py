#Create a function that takes a string and returns that string with the first half lowercased and the last half uppercased.
def sillycase(silly):
    mid = (len(silly)+1) // 2 #add 1 to make divisible midpoint
    return silly[:mid].lower() + silly[mid:].upper()