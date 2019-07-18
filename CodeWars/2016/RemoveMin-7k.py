#Given an array of integers, remove the smallest value. If empty, return empty array.
def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers

