class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1Idx = {n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        
        return res


"""
Approaches I took:
    1. O(n^2) solution
    For each element in "nums1", iterate through "nums2" and find the next greater
    element

Actual Approach:
    1. O(n) solution
    We use a stack to keep a memory of the elements that we came across and if we ever
    come across a element that is greater than the top of the stack, then we pop that
    element and store its answer. The stack will only have elements present in "num1"
    and it will always be in descending order
"""