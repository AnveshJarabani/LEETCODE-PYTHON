"""
Island Count
Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.
"""
# ? THIS IS THE BFS ----------------------------------------------------------------
from collections import deque


def get_number_of_islands(matrix):
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0

    def valid(x, y):
        return (
            0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not visited[x][y]
        )

    def bfs(x, y):
        visited[x][y] = True
        q = deque([(x, y)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            cur_x, cur_y = q.popleft()
            for dx, dy in directions:
                nx, ny = cur_x + dx, cur_y + dy
                if valid(nx, ny):
                    visited[nx][ny] = True
                    q.append((nx, ny))

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                count += 1
                bfs(i, j)
    return count


binaryMatrix = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1],
]
print(get_number_of_islands(binaryMatrix))


# ? THIS IS DFS ----------------------------------------------------------------
def countIslands(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0

    def is_valid(x, y):
        return (
            0 <= x < rows
            and 0 <= y < cols
            and matrix[x][y] == "1"
            and not visited[x][y]
        )

    def dfs(x, y):
        visited[x][y] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                dfs(nx, ny)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1" and not visited[i][j]:
                count += 1
                dfs(i, j)

    return count

def islands(matrix):
    if not matrix:
        return 0
    rows,cols=len(matrix),len(matrix[0])
    visited=[[False for _ in range(rows)] for _ in range(cols)]
    dirs=[[0,1],[1,0],[0,-1],[-1,0]]
    def visit(x,y):
        return matrix[x][y]==1 and not visited and 0<=x<rows and 0<=y<cols
    def bfs(x,y):
        q=deque([x,y])
        visited[x][y]=True
        while q:
            cx,cy=q.popleft()
            for dx,dy in dirs:
                nx,ny=cx+dx,cy+dy
                if visit(nx,ny):
                    visited[nx][ny]=True
                    