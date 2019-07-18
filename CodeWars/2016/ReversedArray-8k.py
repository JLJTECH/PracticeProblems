#Return the digits of n within an array in reverse order.
def digitize(n):
    return [int(d) for d in reversed(str(n))]

#Alternate Solution
def digitize(n):
    return map(int, str(n)[::-1])
