#Return array formatted 8675309 => [8,6,7,5,3,0,9]
def digitize(n):
    return [int(d) for d in str(n)]