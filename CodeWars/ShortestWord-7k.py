#Given a string of words, return the length of the shortest word(s).
def find_short(s):
    return len(min(s.split(), key=len))

