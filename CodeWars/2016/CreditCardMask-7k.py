#write a function which changes all but the last four characters of a string into '#'
def maskify(cc):
    Fr = cc[0:-4]
    return "x" * len(Fr) + cc[-4:]

#Alternate Solution
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]