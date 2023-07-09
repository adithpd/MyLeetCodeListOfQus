class Solution:
    def solveWordWrap(self, nums, k):
        def rec(i,rem,nums,k):
            if (i==len(nums)): #End Of All Words
                return 0

            if (dp[i][rem]!=-1): #Checking if value has been previously calculated and stored in dp array
                return dp[i][rem]
            
            ans = 0 #Variable for storing cost
            
            if (nums[i]>rem): #If number of characters of word is greater than available space
                ans = (rem+1)**2 + rec(i+1,k-nums[i]-1,nums,k)
                
            else:
                choice1 = (rem+1)**2 + rec(i+1,k-nums[i]-1,nums,k) #If we insert the word in next line
                choice2 = rec(i+1,rem-nums[i]-1,nums,k) #If we insert the word in the same line
                ans = min(choice1,choice2)
            
            dp[i][rem] = ans
            return dp[i][rem]
    
        dp = [[-1 for j in range(2005)] for i in range(505)]
        return rec(0,k,nums,k)
    
    
"""
Approach I took:
    1.O(n^2)
    Took a greedy approach only to realize that it won't work
Actual Approach:
    1.O(n^2)
    We need to use recursion and optimize our solution with
    memoization
"""