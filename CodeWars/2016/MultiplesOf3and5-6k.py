#Return the sum of all the multiples of 3 or 5 below the number passed in.
def solution(number):
    lit = []
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            lit.append(i)
    return sum(lit)

#Alternate Solution
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)