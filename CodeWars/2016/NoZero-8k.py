#Remove zero's from end of input
def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n
