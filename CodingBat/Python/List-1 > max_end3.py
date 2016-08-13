def max_end3(nums):
  if nums[0] > nums[-1]:
    i = nums[0]
  else:
    i = nums[-1]
  return [i,i,i]