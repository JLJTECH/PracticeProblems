#Take first line input
s = input()
#Take second line inputs eg..'5 k'
i, c = input().split()
#Print slice from start to i - add c to string, print everything after c
print (s[:int(i)] + c + s[int(i)+1:])