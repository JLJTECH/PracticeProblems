#Check for Prime numbers
def is_prime(n):
    if n >= 2:
        for y in range(2,n):
            if not ( n % y ):
                return False
    else:
        return False
    return True

#Alternate Solution
def is_prime(n):
  return n > 1 and all(n % i for i in xrange(2, n))