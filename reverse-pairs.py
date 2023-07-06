class Solution(object):
    #Merge Sort Approach
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(arr, low, mid, high):
            temp = []  # temporary array
            left = low  # starting index of left half of arr
            right = mid + 1  # starting index of right half of arr

            # storing elements in the temporary array in a sorted manner
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1

            # if elements on the left half are still left
            while left <= mid:
                temp.append(arr[left])
                left += 1

            # if elements on the right half are still left
            while right <= high:
                temp.append(arr[right])
                right += 1

            # transferring all elements from temporary to arr
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
            

            
        def countPairs(arr, low, mid, high):
            right = mid + 1
            cnt = 0
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                cnt += (right - (mid + 1))
            return cnt



        def mergeSort(arr, low, high):
            cnt = 0
            if low >= high:
                return cnt
            mid = (low + high) // 2
            cnt += mergeSort(arr, low, mid)  # left half
            cnt += mergeSort(arr, mid + 1, high)  # right half
            cnt += countPairs(arr, low, mid, high)  # Modification
            merge(arr, low, mid, high)  # merging sorted halves
            return cnt
        
        return mergeSort(nums, 0, len(nums) - 1)
    
    
    
"""
Approach I took:
    1.O(n^2)
    Traverse and search using inner loop to check if required condition meets
    and increment count
    
Actual Approach:
    1.O(n*log(n))
    This involves the Merge Sort technique by checking the required condition
    with left and right halves and correspondingly incrementing count
"""