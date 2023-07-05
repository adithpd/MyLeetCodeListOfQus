class Solution(object):
    #Print Loopwise from outside to inside
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        leftc, rightc = 0, len(matrix[0])-1
        topr, bottomr = 0, len(matrix)-1
        answer = []
        while leftc<=rightc and topr<=bottomr:
            for i in range(leftc,rightc+1):
                answer.append(matrix[topr][i])
            
            for i in range(topr+1,bottomr+1):
                answer.append(matrix[i][rightc])
            
            if topr!=bottomr:
                for i in range(rightc-1,leftc-1,-1):
                    answer.append(matrix[bottomr][i])
            
            if leftc!=rightc:
                for i in range(bottomr-1,topr,-1):
                    answer.append(matrix[i][leftc])
            
            leftc+=1
            rightc-=1
            topr+=1
            bottomr-=1

        return answer