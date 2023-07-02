class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0





"""
Mistake I keep making:
    Code:
        def test(a):    
            a = [x for x in a if x!=0]
            print(a)

        a = [0,1,0,3,12]
        test(a)
        print(a)

    Output:
        [1, 3, 12]
        [0, 1, 0, 3, 12]

    Explanation:
        List is a mutable object. Whenever we try to initialize a list, 
        variable "a" points to the new list created by "[x for x in a if x!=0]". So the variable "a"
        is basically a pointer to a memory location. So we did not mutate the original list outside the function.
    
    Solution:
        #Re-initialization
        a[:] = [x for x in a if x!=0]

        #Copying a list without variable "b" pointing to variable "a"
        b = a[:]
        
        #Shallow copy (Changes made in nested lists inside "a" will affect "b" too)
        b = a.copy() 

        #Deep Copy (Safest way to copy lists with nested lists)
        import copy
        b = copy.deepcopy(a) 
"""     