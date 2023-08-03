class Solution:
    def makesquare(self, matchsticks):
        n = len(matchsticks)
        
        # We don't even have 4 matchsticks to form a square
        if n < 4:
            return False
    
        matchsticks_sum = sum(matchsticks)
        
        # Can't divide into 4 equal sides
        if matchsticks_sum % 4 != 0:
            return False
        
        # The size of each side
        side = matchsticks_sum // 4
        
        # Simulate the square. We will fill the sides in the DFS
        square_sides = [0,0,0,0]
        
        # Sort to optimize the DFS by exiting early because we will start with the biggest elements
        matchsticks.sort(reverse=True)
        
        def dfs(i):
            if i == n:
                side_a = square_sides[0]
                side_b = square_sides[1] 
                side_c = square_sides[2] 
                side_d = square_sides[3] 
                
                # Return true only if all sides are equal to the "side" size we are looking for
                return side == side_a == side_b == side_c == side_d
        
            for side_i in range(4):
                
                if square_sides[side_i] + matchsticks[i] > side:
                    continue
                    
                # Add the matchstick size to the side of the box
                square_sides[side_i] += matchsticks[i]
                
                if dfs(i + 1):
                    return True
                
                # Backtrack if we didn't find the answer
                square_sides[side_i] -= matchsticks[i]
            
            return False
        
        
        return dfs(0)