#CodeFights Intro Gates
#Candies
#Determine how many pieces of candy will be eaten by all the children together

def candies(n, m):
    if m % n == 0:
        return int((m / n) * n)
    elif n == 1:
        return m
    else:
        return int(((m - 1) / n) * n)
