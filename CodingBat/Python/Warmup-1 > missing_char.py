#Warmup-1 > missing_char
def missing_char(str, n):
    l = list(str)
    l.pop(n)
    return ''.join(l)