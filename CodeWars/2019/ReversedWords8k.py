#Complete the solution so that it reverses all of the words within the string passed in.

def reverseWords(str):
  #Split the string into a new list at the spaces
    nstr = str.split(' ')
    
    #iterate backwards then join the string together at the spaces
    return ' '.join(nstr[::-1])

#shorter
  return " ".join(str.split(" ")[::-1])
