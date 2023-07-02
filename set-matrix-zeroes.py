class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        marked_rows = set()
        marked_cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    marked_rows.add(row)
                    marked_cols.add(col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row in marked_rows) or (col in marked_cols):
                    matrix[row][col] = 0
        
        return matrix