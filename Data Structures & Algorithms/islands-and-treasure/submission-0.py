class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW,COL = len(grid), len(grid[0])
        def dfs(x,y, dis):
            if x >= ROW or x < 0 or y >= COL or y < 0 or (grid[x][y] == 0 and dis !=0) or grid[x][y] == -1:
                return
            if grid[x][y] < dis:
                return
            else:
                grid[x][y] = dis
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(x+dx,y+dy,dis+1)


            

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    dfs(i,j,0)

