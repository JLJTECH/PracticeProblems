#Python reminders

# Collapse the list
''.join(list) 

#Count occurrences of item in list
[a,b,c,d,e].count(item) 

#put anything in square brackets to search list index
a[0] 

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

#Use F strings
x = "hello"
w = "world"
print(f"{x} {w}")

#List comprehensions
	#example CW solution used to reverse all words >= 5 letters and print out the modified sentence
	[word[::-1] if len(word) >= 5 else word for word in words]

#Collapse multiple inputs into one
	#from this
	def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
	#to this
	def predict_age(*ages)

