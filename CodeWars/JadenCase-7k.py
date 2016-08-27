#Return an array
def toJadenCase(string):
   return  " ".join(w.capitalize() for w in string.split())

#Alternate Solution (Breaks on posessives i.e. You'Re)
def toJadenCase(string):
    return string.title()