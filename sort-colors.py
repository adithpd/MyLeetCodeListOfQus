class Solution(object):
    #Dutch National Flag Problem using 3-Pointers
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1
        while(mid<=high):
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low+=1
                mid+=1

            elif nums[mid] == 1:
                mid+=1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1


"""
Approach I took:
    1.O(nlogn)
    Thought Of Sorting Algorithms like QuickSort and
    MergeSort
    
    2.O(n)
    Used a hashmap approach by storing counts and then
    finally replacing the array values in sorted order
    
Actual Approach:
    1.O(n)
    This is a Dutch National Flag problem that can be
    solved using the 3-Pointer Approach
"""