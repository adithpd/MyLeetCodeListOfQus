class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(m+1)]
        for str in strs:
            one = 0
            zero = 0
            for c in str:
                if c == '1':
                    one += 1
                else:
                    zero += 1
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    if one <= j and zero <= i:
                        dp[i][j] = max(dp[i][j], dp[i-zero][j-one] + 1)
        return dp[m][n]