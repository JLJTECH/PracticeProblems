#Python 3 - Data Types - List Problem

z = int(input())
L = []
count = 0
#start for loop
for _ in range(z):
    #set command variable
    command = input().split()
    if "insert" in command:
        L.insert(int(command[1]), int(command[2]))
    elif "append" in command:
        L.append(int(command[1]))
    elif "remove" in command:
        L.remove(int(command[1]))
    elif "pop" in command:
        L.pop()
    elif "sort" in command:
        L.sort()
    elif "reverse" in command:
        L.reverse()
    elif "count" in command:
        L.count()    
    else:
        print (L)
