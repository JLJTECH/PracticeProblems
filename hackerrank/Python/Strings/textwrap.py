#import the textwrap module
import textwrap
#use the .fill method and take 2 inputs - First takes string, second takes int for length of wrapping
a = textwrap.fill(input(), int(input()))
print (a)
