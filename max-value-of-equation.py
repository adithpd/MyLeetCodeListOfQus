class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        maxEqValue = float('-inf')
        dequeue = []
        j = 0
        while j<len(points): #Iterating through the coordinates array
            xj = points[j][0] #Extracting the x-coordinate
            yj = points[j][1] #Extracting the y-coordinate

            while dequeue and (xj - dequeue[0][1]>k): #Removing previously stored "yi-xi" values where "xj-xi > k" from beginning of dequeue
                dequeue.pop(0)
            
            if dequeue: #Comparing and storing the maximum value of equation "yj + xj + (yi - xi)"
                maxEqValue = max(maxEqValue, yj + xj + dequeue[0][0])

            while dequeue and dequeue[-1][0] < yj - xj: #Removing all previous "yi-xi" values from dequeue smaller than "xj-yj" from end
                dequeue.pop()
            
            dequeue.append((yj - xj, xj)) #Adding the current "yj-xj" as "yi-xi" value to dequeue
            j+=1 #Next Index
        
        return maxEqValue
    
    
"""
This problem was pretty difficult to me. Easy to get to O(n^2) but not 
the O(n) solution. For this we have to decode the logic and understand
when to use priority queues

The problem is even better as the coordinates array is sorted in ascending
order of x-coordinates

Find maximum of "yi + yj + |xi - xj|" where "xi < xj" is same as telling you
Find maximum of "yi + yj -(xi - xj)"

So the above eqn can be rewritten as, (yj+xj) + (yi-xi)
Now the problem boils down to finding maximum in sliding window of k size.
"""