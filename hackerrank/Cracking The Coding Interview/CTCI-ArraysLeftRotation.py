#Cracking The Coding Interview - Arrays: Left Rotation
def array_left_rotation(a, n, k):
    AL = list(a)
    V = AL[k:]+AL[:k]
    return V