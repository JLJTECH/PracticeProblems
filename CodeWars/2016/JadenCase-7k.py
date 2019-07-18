#Return string with all first characters as caps
def toJadenCase(string):
   return  " ".join(w.capitalize() for w in string.split())

#Alternate Solution (Breaks on posessives i.e. You'Re)
def toJadenCase(string):
    return string.title()
