#Python reminders - those pesky Gotchas!

''.join(list) # Collapse the list

[a,b,c,d,e].count(item) #Count occurrences of item in list

a[0] #put anything in square brackets to search list index

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
