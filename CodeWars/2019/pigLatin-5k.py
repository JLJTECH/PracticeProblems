#!/usr/bin/env python3

'''
Create a Pig Latin converter. Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
'''

def pig_it(text):
    words = text.split(" ")
    pl_words = []
    for i in words:
      if i.isalpha():
        if len(i) > 1:
          pl_words.append(i[1:]+i[0] + 'ay')
        else:
          pl_words.append(i + 'ay')
      else:
        pl_words.append(i)
    pl_text = ' '.join(pl_words)
    return pl_text
    
    
#Alternative implementations
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
        
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
