#Return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
def sum_two_smallest_numbers(numbers):
    st = sorted(numbers)
    return st[0] + st[1]


#Alternate Solution
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])