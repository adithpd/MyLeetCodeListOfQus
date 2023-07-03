class Solution:
  def removeDuplicates(self, nums):
    if len(nums) == 1:
        return 1
    
    index = 1
    while index < len(nums):
        if nums[index-1] == nums[index]:
            nums.pop(index-1)
        else:
            index+=1
    
    return len(nums)