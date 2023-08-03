class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        search = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    search.append([i,j])
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]

        def dfs(i,j,grid,visited):
            if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0:
                return 0

            if grid[i][j] == 0:
                return 0
            
            if visited[i][j]:
                return 0

            if not visited[i][j]:
                visited[i][j] = True
                return 1 + dfs(i-1,j,grid,visited) + dfs(i+1,j,grid,visited) + dfs(i,j-1,grid,visited) + dfs(i,j+1,grid,visited)

        maxx = 0
        for i,j in search:
            maxx = max(dfs(i,j,grid,visited), maxx)
        
        return maxx