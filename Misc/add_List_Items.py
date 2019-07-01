#!/usr/bin/env Python3
'''
A number is input in computer then a new no should get printed by adding one to each of its digit. 
If you encounter a 9, insert a 10 (don't carry over, just shift things around).
For example, 998 becomes 10109
'''

def changer(val):

  #Convert value to String  
  a = str(val)
  #Put string values in list
  b = list(a)
  #loop over values, add intigers, convert to string
  c = [str(1+int(i)) for i in b]
  #join list and remove commas
  print(','.join(c).replace(',',''))

changer(998)
