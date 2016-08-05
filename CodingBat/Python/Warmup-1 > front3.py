#Warmup-1 > front3
def front3(str):
  first3 = str[:3]
  if len(str) > 3:
    return first3 * 3
  else:
    return str * 3