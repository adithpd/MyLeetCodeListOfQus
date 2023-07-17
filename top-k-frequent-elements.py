class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mini = min(nums)
        bucket = [[i,0] for i in range(mini,max(nums)+1)]
        for i in nums:
            bucket[i-mini][1]+=1
        
        bucket.sort(reverse=True, key=lambda x: x[1])
        answer = [ bucket[i][0] for i in range(k)]

        return answer