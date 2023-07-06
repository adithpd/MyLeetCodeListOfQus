class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        element = nums[0]
        size = len(nums)
        for i in range(1,size):
            if count == 0:
                element = nums[i]
                count = 1

            elif nums[i] != element:
                count-=1
            
            else:
                count+=1
        
        return element
    


"""
Approach I took:
    1.O(n^2)
    Traverse and search using inner loop to check if element repeats
    greater than "n//2" or "floor(n/2)"
    
    2.O(n)
    Used a hashmap approach by storing counts and then
    finally finding "key" with maximum "value"
    
Actual Approach:
    1.O(n)
    This is a Moore's Voting Algorithm problem that can be
    solved using voter and anti-voter approach
"""