#Return true or false depending upon whether the given number, each raised to the power of the number of digits is equal to the sum of its own digits.

def narcissistic( value ):
    s1 = list(str(value))
    s2 = len(s1)
    if sum(int(i) ** s2 for i in s1) == value:
        return True
    else:
        return False


#Alternate Solution
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))