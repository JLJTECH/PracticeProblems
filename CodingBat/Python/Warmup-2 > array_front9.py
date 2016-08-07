def array_front9(nums):
  for i in nums:
    if 9 in nums[:4]:
      return True
  return False
    