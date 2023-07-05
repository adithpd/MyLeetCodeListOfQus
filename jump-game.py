class Solution(object):
    #Greedy Approach from end position
    #You can do it from starting too
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        marker = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= marker:
                marker = i
        
        return True if marker==0 else False