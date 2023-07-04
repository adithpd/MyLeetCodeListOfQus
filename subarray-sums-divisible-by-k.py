class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = dict()
        hashmap[0] = 1
        Sum = 0; count = 0
        for i in range(len(nums)):
            Sum += nums[i]
            remainder = Sum % k
            if remainder in hashmap:
                count+=hashmap[remainder]
                hashmap[remainder]+=1
            else:
                hashmap[remainder]=1

        return count
    



"""
Approach I took:
    1.O(n^3)
    I traversed the entire array to find all possible subarrays
    whose sum is divisible by "k"
    
    2.O(n^2)
    You can optimize the above solution by storing sum in a variable
    rather than recalculating it over and over again
    
Actual Approach:
    1.O(n)
    This problem is based on the prefix sum problem. So we find the sum
    as we traverse the array in a single pass. We find the remainder
    when divided by "k" and check if we have previously come across the same
    remainder. If so we can say that there is a subarray divisible by "k"
    as 'modulo theory' states that if two numbers have the same remainder
    when divided by "k" then there difference is divisible by "k" 
"""