#Given a number, find its opposite.
def opposite(number):
    if number > 0:
        return -number
    else:
        return abs(number)

#Alternate Solution
def opposite(number):
    return -number