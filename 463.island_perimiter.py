def island(grid):
    visit=set()
    
    def dfs(i,j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) \
            or grid[i][j] == 0:
                return 1
        if (i,j) in visit:
            return 0
        visit.add((i,j))
        peri=dfs(i-1,j)
        peri+=dfs(i+1,j)
        peri+=dfs(i,j-1)
        peri+=dfs(i,j+1)
        return peri
    
    
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:return dfs(i,j)

grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(island(grid))