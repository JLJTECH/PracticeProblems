#Given a non-negative integer, return an array / a list of the individual digits in order.
def largest(n,xs):
  xss = sorted(xs, reverse=True)
  return sorted(xss[:n])


#Alternate Solution
def largest(n,xs):
	return sorted(xs)[-n:];