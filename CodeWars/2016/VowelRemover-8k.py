#Create a function called shortcut to remove all the lowercase vowels in a given string.
def shortcut( s ):
    return ''.join(char for char in s if char not in set('aeiou'))


#Alternate Solution
def shortcut(s):
    return s.translate(None, 'aeiou')