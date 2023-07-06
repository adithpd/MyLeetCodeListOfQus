class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        birth = []
        die = []

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == 0:
                    count = 0
                    if j-1 >= 0:
                        if board[i][j-1] == 1:
                            count+=1

                        if i+1 < len(board):
                            if board[i+1][j-1] == 1:
                                count+=1

                        if i-1 >= 0:
                            if board[i-1][j-1] == 1:
                                count+=1
                    
                    if i-1 >= 0:
                        if board[i-1][j] == 1:
                            count+=1

                    if i+1<len(board):
                        if board[i+1][j] == 1:
                            count+=1
                    
                    if j+1 < len(board[0]):
                        if board[i][j+1] == 1:
                            count+=1
                        
                        if i+1 < len(board):
                            if board[i+1][j+1] == 1:
                                count+=1

                        if i-1 >= 0:
                            if board[i-1][j+1] == 1:
                                count+=1
                
                    if count == 3:
                        birth.append([i,j])
                    
                if board[i][j] == 1:
                    count = 0
                    if j-1 >= 0:
                        if board[i][j-1] == 1:
                            count+=1

                        if i+1 < len(board):
                            if board[i+1][j-1] == 1:
                                count+=1

                        if i-1 >= 0:
                            if board[i-1][j-1] == 1:
                                count+=1
                    
                    if i-1 >= 0:
                        if board[i-1][j] == 1:
                            count+=1

                    if i+1<len(board):
                        if board[i+1][j] == 1:
                            count+=1
                    
                    if j+1 < len(board[0]):
                        if board[i][j+1] == 1:
                            count+=1
                        
                        if i+1 < len(board):
                            if board[i+1][j+1] == 1:
                                count+=1

                        if i-1 >= 0:
                            if board[i-1][j+1] == 1:
                                count+=1
                    
                    if count < 2:
                        die.append([i,j])
                    
                    if count > 3:
                        die.append([i,j])
        
        for row,col in die:
            board[row][col] = 0
        
        for row,col in birth:
            board[row][col] = 1