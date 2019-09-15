#!/usr/bin/env python3
'''
Write a function that accepts a string and an n and returns a cipher by rolling each character forward (n > 0) or backward (n < 0) n times.
'''
def rolling_cipher(txt, n):
  cipher = ""
  for i in range(len(txt)):
    char = txt[i]
    cipher += chr((ord(char) + n - 97) % 26 + 97)
  return cipher
 
#Alternative Solutions
def rolling_cipher(txt, n):
  lets = 'abcdefghijklmnopqrstuvwxyz'
  result = ''
  for char in txt:
    result += lets[(lets.index(char)+n)%26]
  return result
