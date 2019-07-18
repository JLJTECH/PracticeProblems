#It is simple if: the length of each word does not exceed the amount of words in the string. Else, it is complex

def is_kiss(words):
    wl = words.split()
    ws = len(wl)
    for w in wl:
        if len(w) > ws:
            return "Keep It Simple Stupid"
    return "Good work Joe!"


#Alternate Solution
def is_kiss(words):
    return "Keep It Simple Stupid" if max(len(i) for i in words.split())>len(words.split()) else "Good work Joe!"
