def findMinDiff(arr, n):
    #Edge Cases
    if n>len(arr):
        return -1
    if n == 0 or len(arr) == 0:
        return 0
    
    #Sorting the array
    arr.sort()
    
    min_diff = float("inf")
    
    #Sliding window approach using two pointers
    left = 0
    for right in range(n-1,len(arr)):
        min_diff = min(min_diff, arr[right]-arr[left])
    
    return min_diff 