#Take a list and return an exact copy.

def copy_list(l):
  new_copy = l[:]
  return new_copy


#Alternate Solution
def copy_list(l):
	return list(l)