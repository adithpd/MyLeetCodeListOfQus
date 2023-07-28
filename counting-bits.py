class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def ones(n):
            w = 0
            while (n):
                w += 1
                n &= n - 1
            return w
        
        answer = []
        for i in range(n+1):
            answer.append(ones(i))
            
        return answer