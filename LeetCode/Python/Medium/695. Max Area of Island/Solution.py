class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:    
                    grid[i][j] = 0
                    q = []
                    q.append([i,j])
                    count = 0
                    while(len(q)>0):
                        r,c = q.pop(0)
                        count += 1
                        directions = [[0,1],[1,0],[-1,0],[0,-1]]
                        for dr,dc in directions:
                            nr = r+dr
                            nc = c+ dc
                            if(0<=nr<m and 0<=nc<n and grid[nr][nc] == 1):
                                grid[nr][nc]= 0
                                q.append([nr,nc])
                    maxi = max(maxi,count)

        return maxi
        

        