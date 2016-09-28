#You will be given a string of four words. Your job is to turn them in to foul language.
#words should be Caps, Every word should end with '!!!!', Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.
def gordon(a):
    a = a.upper()
    a = a.replace(' ', '!!!! ')
    a = a.replace('A', '@')
    VL = ['E', 'I', 'O', 'U']
    for i in VL:
        a = a.replace(i, '*')
    return a + '!!!!'


