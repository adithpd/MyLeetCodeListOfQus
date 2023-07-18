class Solution(object):
    #Dynamic Programming and Pointer Based Approach
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n)]
        dp[0] = 1
        p1 = 0
        p2 = 0
        p3 = 0
        for i in range(1,n):
            twoMultiple = dp[p1]*2
            threeMultiple = dp[p2]*3
            fiveMultiple = dp[p3]*5
            dp[i] = min(twoMultiple,threeMultiple,fiveMultiple)

            if dp[i]==twoMultiple:p1+=1
            if dp[i]==threeMultiple:p2+=1
            if dp[i]==fiveMultiple:p3+=1
        
        return dp[-1]