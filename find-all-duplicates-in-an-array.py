class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index]<0:
                output.append(index+1)
            nums[index] = -nums[index]
        
        return output



"""
Approach I took:
    Thought of Floyd Cycle Detection Algorithm
    
Actual Approach:
    1.O(n)
    This problem is a trick question. You want to traverse the array and each
    value is an index. You go to that index and check if that element is negative
    if not we make it negative to indicate it has been visited else it means
    that the "pointed-index + 1" is a duplicate 
"""