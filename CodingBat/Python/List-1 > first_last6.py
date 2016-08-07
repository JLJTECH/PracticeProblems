def first_last6(nums):
  for i in nums:
    if 6 == nums[0] or 6 == nums[-1]:
      return True
  return False
    