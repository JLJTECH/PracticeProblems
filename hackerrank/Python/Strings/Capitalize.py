#Capitalize the first letter of each word from stdin. Strip whitespace and ignore strings starting with numbers.
print(" ".join((s.capitalize() for s in input().strip().split(" "))))