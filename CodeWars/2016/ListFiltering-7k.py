#Return a new list with the strings filtered out
def filter_list(l):
  return [x for x in l if type(x) is not str]
