def array_front9(nums):
  if len(nums) <= 4:
    for num in nums:
      if num == 9:
        return True
  else:
    for i in range(0, 4):
      if nums[i] == 9:
        return True
  return False
