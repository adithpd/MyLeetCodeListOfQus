class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        left = [0 for i in range(len(heights))]
        right = [0 for i in range(len(heights))]
        #Max possible left boundary finder
        for i in range(len(heights)):
            if (stack == []):
                left[i] = 0

            elif (heights[i] <= heights[stack[-1]]):
                while (stack!=[] and heights[i] <= heights[stack[-1]]):
                    stack.pop()
                if (stack==[]):
                    left[i] = 0
                else:
                    left[i] = stack[-1] + 1

            else:
                left[i] = stack[-1] + 1
            
            stack.append(i)
        #Max possible right boundary finder
        stack = []

        for i in range(len(heights)-1,-1,-1):
            if (stack == []):
                right[i] = len(heights)-1

            elif (heights[i] <= heights[stack[-1]]):
                while (stack!=[] and heights[i] <= heights[stack[-1]]):
                    stack.pop()
                if (stack==[]):
                    right[i] = len(heights)-1
                else:
                    right[i] = stack[-1] - 1

            else:
                right[i] = stack[-1] - 1
            
            stack.append(i)
        
        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i]*(right[i]-left[i]+1))
        
        return res





class Solution(object):
    #Faster and Efficient
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))
        
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        
        return maxArea



"""
Actual Approach:
    1.O(n)
    So we find the sum as we traverse the array in a single pass and use
    a stack to store previous heights and indices
"""