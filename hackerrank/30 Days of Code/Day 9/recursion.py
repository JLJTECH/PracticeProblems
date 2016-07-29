#Recursion problem - Task: Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).

def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

print(factorial(int(input())))