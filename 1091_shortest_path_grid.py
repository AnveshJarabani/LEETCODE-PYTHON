class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        span=len(grid)-1
        q=deque()
        q.append((0,0,1)) # initial row,col,path_length
        paths=[[0,1],[1,0],[0,-1],[-1,0],
                [1,1],[-1,-1],[-1,1],[1,-1]]
        visited=set()
        visited.add((0,0)) #visited paths
        while q:
            r,c,l=q.popleft()
            if min(r,c)<0 or max(r,c)>span or grid[r][c]:
                continue
            if (r,c)==(span,span):
                return l
            for r_p,c_p in paths:
                if (r+r_p,c+c_p) not in visited:
                    q.append((r+r_p,c+c_p,l+1))
                    visited.add((r+r_p,c+c_p))
        return -1