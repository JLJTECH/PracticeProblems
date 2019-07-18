#Implement an difference function, which subtracts one list from another.
def array_diff(a, b):   
    if b == []:
        return a
    else:
        return list(x for x in a if x not in b)

#Alternate Solution
def array_diff(a, b):
    return [x for x in a if x not in b]
