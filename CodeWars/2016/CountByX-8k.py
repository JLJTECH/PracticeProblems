#Create a function with two arguments that will return a list of length (n) with multiples of (x).
def count_by(x, n):
    return list(range(x,x*n+1,x))

#Alternate Solution
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]