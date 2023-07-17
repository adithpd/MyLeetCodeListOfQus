class Solution(object):
    #Quick Select Algorithm
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums)-k

        def QuickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p]

            if k > p:
                return QuickSelect(p+1,r)
            elif k < p:
                return QuickSelect(l, p-1)
            else:
                return nums[p]
        
        return QuickSelect(0,len(nums)-1)
    
    
class Solution(object):
    #Heap Method
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #heapq.heapify(list)
        #heapq.nlargest(k,list)
        #heapq.smallest(k,list)
        #heapq.heappop(heap form of listm)
        #heapq.heappush(heap form of list, value)
        import heapq
        
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        for i in range(k - 1):
            heapq.heappop(max_heap)
        return -max_heap[0]

"""
    Actual Approach:
    1.O(logn)
    A Max/Min Heap is created and accordingly we pop elements until
    we get the "k"-th largest.
    
    2.O(n^2)
    Quick Select Algorithm is expected. It involves using a pivot
    and partioning the array. We then finally check if the "index
    marker" and "k" both fall at same place, if not we rerun the 
    algorithm on either the left/right part of the partitioned array.
"""