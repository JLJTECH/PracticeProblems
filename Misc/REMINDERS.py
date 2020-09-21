#Python reminders

# Collapse the list for output
''.join(list)
#Collapse and convert items to string
''.join(map(str, lst))

#Flatten list of lists
flat_list = [item for subitem in lists for item in subitem]

#Exammple for checking list for single digit (string)
def checker(string):
	print("Boom!" if "7" in str(string) else "there is no 7 in the list")
checker([2, 55, 60, 97, 86, 3, 4, 6, 6])

#Check list for letters or numbers
letters = ''.join(x for x in item if x.isalpha())
digits = ''.join(x for x in item if x.isnumeric())

#Scan list for longest string and print max item
print(max(len(i) for i in string.split()))

#Search for highest index of substring
string.rindex(substring) -- If not found, raises exception
string.rfind(substring) -- If not found, returns -1

#Dont forget min and max
max(x) for largest
min(x) for smallest

#Count occurrences of item in list
[a,b,c,d,e].count(item)
sum([x.count(letter) for x in lst])

#Use Regex to count all lowercase letters in given string.
import re
def lowercase_count(string):
    return len(re.findall('[a-z]',string))

#Count Sublists in list
return str(lst).count('[') - 1
return sum(1 for i in lst if type(i)==list)
return sum(isinstance(i, list) for i in lst)

#Count occurrences of list 1 items in list 2
value =  len([i for i in list2 if i in list1 ])

#Put anything in square brackets to search list index
a[0]
#Reverse list of ints by converting to string and list reversing
str(num)[::-1]

#Strange list rotation
def rotate_left3(nums):
  a = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = a
  return nums -> [1,2,3] = [2,3,1]

#Evaluator positioning
if someting:
	return (item 1 >= 10)
else:
	return (item > 1 and item <= 5)

#One line conditionals
	#get item index from lst, not there, return -1
return lst.index(item) if item in lst else -1

#Use F strings
x = "hello"
w = "world"
print(f"{x} {w}")

#Aligning text
print('{:<10}'.format('X')) # left align
X         
print('{:>10}'.format('X')) # right align
         X
print('{:^10}'.format('X')) # center
    X     
print('{:?^10}'.format('X')) # add a fill character
????X?????

#Using commas as a delimiter
print('{:,}'.format(2783727282727)) 
2,783,727,282,727

print('{:.2%}'.format(90.60/100))   
90.60%

#Use Swapcase to flip lowercase and uppercase
string.swapcase()

#List comprehensions
	#Reverse all words >= 5 letters and print out the modified sentence
	[word[::-1] if len(word) >= 5 else word for word in words]
	#Create a dictionary of letters and their frequency of occurrence in a string
	{i : message.count(i) for i in set(message)}
	#List all indexes of a specified value
	def get_indicies(lst, el):
	[i for i in range(len(lst)) if lst[i] == el]
	#Edabit solution for odd occurrence of item in list
	[i for i in lst if lst.count(i) % 2 > 0]
	#Only return the integers in a list
	[x for x in l if type(x) == int]
	#Flatten list of lists
	flat_list = [item for subitem in lists for item in subitem]
	#Split int into list of digits
	split_number = [int(d) for d in str(n)]
	#Dictionary values for item
	value = [str(dictionary[i]) for i in string]
	#list character index from left to right, right to left
	[mylist.index(char), mylist.rindex(char)]

#Letter replacements/translations
def correct(string):
    return string.translate(str.maketrans("501", "SOI"))

#Dictionary reminders
dictionary_name.values() - list all values
keys() - list all keys
get() - access value for key
use Dict[1] or Dict[name] - access item via key

#Simple hard coded cipher
def move(word):
	return ''.join(chr(ord(i) + 1) for i in word)
	
#Collapse multiple inputs into one
	#from this
	def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
	#to this
	def predict_age(*ages)

#Remove char
def remove_exclamation_marks(s):
    return s.replace('!', '')

#Replace Vowels with "!"
def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)

#Remove duplicate words, keep index position
def remove_duplicate_words(s):
    return ' '.join(sorted(set(s.split()), key = s.index))

#Quick Lambda implementation on multiple args - with f"string"
def newvibe(a,b,c):
	var1 = lambda x: (x * 5)
	print(f"This is a: {var1(a)}, This is b: {var1(b)}, This is c: {var1(c)}")

#Alternative method to return binary of a number
variable = format(number, "b")

#Boolean type checking
return "boolean expexted" if not isinstance(arg, bool) #Print Boolean expected if arg is not boolean

#Quick counter implementation - Sum vowels in string.
val = sum([1 for x in txt.lower() if x in 'aeiou'])
