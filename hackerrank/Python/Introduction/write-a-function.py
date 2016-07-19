#Python 2 introduction challenge - Write a function.

year = int(raw_input())

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 400 == 0:
        leap = True
    return leap

print is_leap(year)
