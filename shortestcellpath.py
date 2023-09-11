"""Shortest Cell Path
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011"""


def shortestCellPath(grid, sr, sc, tr, tc):
    rows, cols = len(grid), len(grid[0])
    result = [float("inf")]

    def bt(x, y, path_sum, cache_set):
        if (
            x >= rows
            or y >= cols
            or grid[x][y] == 0
            or (x, y) in cache_set
            or x < 0
            or y < 0
        ):
            return 0
        cache_set.add((x, y))
        if x == tr and y == tc:
            result[0] = min(path_sum, result[0])
            return result[0]
        if grid[x][y] == 1:
            path_sum += 1
        bt(x + 1, y, path_sum, cache_set)
        bt(x, y + 1, path_sum, cache_set)
        bt(x - 1, y, path_sum, cache_set)
        bt(x, y - 1, path_sum, cache_set)

    bt(sr, sc, 0, set())
    return result[0] if result[0] != float("inf") else -1


from collections import deque


# BFS ----------------------------------------------------------------
def getNeighbor(row, col, grid):
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    neighbors = []
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if (
            new_row < 0
            or new_row >= len(grid)
            or new_col < 0
            or new_col >= len(grid[0])
            or grid[new_row][new_col] != 1
        ):
            continue
        else:
            neighbors.append((new_row, new_col))

    return neighbors


def shortestCellPath(grid, sr, sc, tr, tc):
    queue = deque([(sr, sc)])
    visited = set((sr, sc))

    target = (tr, tc)

    shortest_path = 0
    while len(queue) > 0:
        size_of_queue = len(queue)
        for i in range(size_of_queue):
            row, col = queue.popleft()
            neighbors = getNeighbor(row, col, grid)
            for neighbor in neighbors:
                if not neighbor in visited:
                    if neighbor == target:
                        return shortest_path + 1
                    visited.add(neighbor)
                    queue.append(neighbor)
        shortest_path += 1
    return -1
