class Solution(object):
    #Recursive Approach
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def recursion(index, buy, prices):
            #Out Of Bounds Condition
            if (index==len(prices)):
                return 0
            
            #Profit Variable
            profit = 0

            #If we buy a stock
            if(buy):
                """
                Finding max profit
                Arg-1: If we purchase stock
                Arg-2: If we don't purchase stock
                """
                profit = max(
                    recursion(index+1,0,prices)-prices[index],
                    recursion(index+1,1,prices)
                )
            #If we don't buy a stock
            else:
                """
                Finding max profit
                Arg-1: If we purchase stock
                Arg-2: If we don't purchase stock
                """
                profit = max(
                    prices[index] + recursion(index+1,1,prices),
                    recursion(index+1,0,prices)
                )

            return profit
        
        return recursion(0,1,prices)
    




class Solution(object):
    #Dynamic Programming Approach
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def recursion(index, buy, prices, dp):
            if (index==len(prices)):
                return 0
            
            if dp[index][buy] != -1:
                return dp[index][buy]

            profit = 0

            if(buy):
                profit = max(
                    recursion(index+1,0,prices,dp)-prices[index],
                    recursion(index+1,1,prices,dp)
                )
            
            else:
                profit = max(
                    prices[index] + recursion(index+1,1,prices,dp),
                    recursion(index+1,0,prices,dp)
                )

            dp[index][buy] = profit
            return dp[index][buy]
        
        dp = [[-1,-1] for _ in range(len(prices))]
        return recursion(0,1,prices,dp)
    
    
    

"""
I couldn't come up with a solution. I was simply stuck
staring at my screen as if my brain froze
    
Actual Approach:
    1.Recursive Approach
    2.DP Approach
    3.Tabulation Approach
"""