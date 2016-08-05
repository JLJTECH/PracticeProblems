def front_times(str, n):
  if len(str) >= 3:
    return str[0:3] * n
  elif len(str) < 3:
    return str * n