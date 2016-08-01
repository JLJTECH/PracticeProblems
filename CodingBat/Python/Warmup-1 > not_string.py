#Warmup-1 > not_string 
def not_string(str):
  if str.startswith('not'):
    return str
  else:
    return "not " + str