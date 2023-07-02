class Solution(object):
    #Greedy Approach
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy = prices[i]

            max_profit = max(max_profit, prices[i] - buy)
        return max_profit
    

class Solution(object):
    #Two Pointer Approach
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            
            else:
                left = right
            
            right+=1 
        return max_profit


"""
Approaches I took:
    1. O(n^2) solution
    //Time Limit Exceeded
    
    2. Using a list "p" which is a sorted copy of the "prices" list.
    I deleted elements as I traversed through the "prices" list. I 
    then used the greatest element in "p" and kept storing "max_profit"
    as "max_profit = max(max_profit, p[-1] - prices[i])"
    //Time Limit Exceeded
    //Too Much Space
    
    3. Thought Of A Two Pointer Approach but couldn't find it

Actual Approach:
    1. O(n) solution
    Greedy Approach by traversing prices while also storing the 
    lowest buy value to maximize profit
    
    2. O(n) solution
    Two Pointer Approach works by traversing the array while also 
    checking if "price[right]>price[left]" and storing "max_profit"
    else "left=right"
"""