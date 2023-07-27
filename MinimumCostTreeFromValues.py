class Solution(object):
    #Greedy Based Approach
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr = [float('inf')] + arr + [float('inf')]
        n, res = len(arr), 0
        
        while n>3:
            mi = min(arr)
            ind = arr.index(mi)
            
            if arr[ind-1]<arr[ind+1]:
                res+=arr[ind-1]*arr[ind]
            else:
                res+=arr[ind+1]*arr[ind]
            
            arr.remove(mi)
            n = len(arr)
        
        return res
    


class Solution(object):
    #Stack Based Approach
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        
        for x in arr:
            while len(stack) and stack[-1] <= x:
                mini = stack.pop() # minimum element of the 3 elements stack[-1], stack[-2] and x
                
                if stack: # if stack has any item left
                    res +=  mini * min(x, stack[-1])
                else:
                    res += mini * x
            
            stack.append(x)
        
        # process the remaining items
        y = stack.pop()
        
        while len(stack):
            z = stack.pop()
            res += y * z
            y = z
        
        return res


"""
Approaches I took:
    I didn't spend my time thinking and was kind of lazy

Actual Approach:
    1. O(n) solution
    This solution is Greedy Approach based,
      ( ) p1 		 					         (  ) p1
	 /   \           						    /    \
	5     ( ) p2						p2    ( )     ( )  p3
		  /  \ 							     /   \	  /  \
	 p3 ( )   4 						    5     2  3    4	
	   /   \
	  2     3
    Consider node 2 which has minimum value , it has 2 options.
    Combine with 3 as in first diagram or combine with 5 as in second diagram
    So it will go for that option which gives minimum product that is 2*3 < 2*5
    So it choose 1st diagram and p3 = 6 . Now we remove the node 2 from array as 
    to compute value for node p2 only node 3 is required because 3>2 and we want 
    max of left leaf node and max of right leaf node So only greater node proceeds
    Array becomes [5,3,4] . Again we find minimum and repeat the process
    
    2. O(n) solution
    This solution is Stack based,
    If we are given 3 elements, we iterate from left to right and multiply the least item 
    to the second least one and keep the second least item and the largest one in a monotonic 
    descending stack. We can only multiply the neighbouring items at any given moment. 
    Note: in these 3 elements, the smallest element can only be used once.  
"""