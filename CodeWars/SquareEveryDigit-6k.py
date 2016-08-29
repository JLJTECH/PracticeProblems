#Square every digit of a passed int
def square_digits(num):
    squares = []
    for i in str(num):
        squares.append(int(i)**2)
    x = ''.join(map(str, squares))
    print(x.replace("'", ""))


#Alternate solution
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
