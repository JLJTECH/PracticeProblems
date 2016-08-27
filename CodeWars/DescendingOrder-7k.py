#Take any non-negative integer as a argument and return it with it's digits in descending order
def Descending_Order(num):
    lit = list(str(num))
    print("".join(sorted(lit, reverse= True)))


#Alternate solution
def Descending_Order(num):
  return int("".join(sorted(str(num), reverse=True)))