class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = dict() #hashmap
        hashmap[0] = 1 #This condition is very important
        preSum = 0; count = 0
        for i in range(len(nums)):#We iterate through the array
            preSum += nums[i]
            remove = preSum - k
            if remove in hashmap:#We check if we have come across this prefix sum before 
                count+=hashmap[remove]

            if preSum in hashmap:#If not present, we simply add current sum to hashmap
                    hashmap[preSum]+=1
            else:
                hashmap[preSum]=1

        return count
    
    
    
    
"""
Approach I took:
    1.O(n^3)
    I traversed the entire array to find all possible subarrays
    whose sum is equal to "k"
    
    2.O(n^2)
    You can optimize the above solution by storing sum in a variable
    rather than recalculating it over and over again
    
Actual Approach:
    1.O(n)
    So we find the sum as we traverse the array in a single pass. 
    We then check if we have come across "current_sum - k" before.
    If so it means we have a subarray whose sum equals "k". 
"""