#use splat (*) to take unknown num of args
def sumAll(*args):
    sum = 0

    for i in args:
        sum += i
    return sum
print(sumAll(2,3,4,5))