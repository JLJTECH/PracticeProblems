#Write a program that finds the summation of every number between 1 and num. The number will always be a positive integer greater than 0.
def summation(num):
    su = 0
    for i in range(num + 1):
        su += i
    return su


#Alternate Solution
def summation(num):
    return sum(xrange(num + 1))