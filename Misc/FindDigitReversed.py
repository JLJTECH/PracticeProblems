#outputs the nth digit of num (counting from right to left).
def find_digit(num, nth):
    num = str(num)
    num = num[::-1] #Reverse num
    return int(num[nth-1])