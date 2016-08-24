#Implement a function that determines whether a string that contains only letters is an isogram.
def is_isogram(string):
    l = list(string.lower())
    return len(l) == len(set(l))

#Alternate Solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))