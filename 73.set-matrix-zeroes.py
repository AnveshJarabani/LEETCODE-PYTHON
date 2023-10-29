from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_count, col_count = len(matrix), len(matrix[0])
        zeros = []
        # for i in range(row_count):
        #     for j in range(col_count):
        #         if matrix[i][j] == 0:
        zeros = [
            (i, j)
            for i in range(row_count)
            for j in range(col_count)
            if matrix[i][j] == 0
        ]
        for i, j in zeros:
            matrix[i] = [0] * col_count
            for i in range(row_count):
                matrix[i][j] = 0
        return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(Solution().setZeroes(matrix))


"""
for i in row:
    for j in i:
    if matrix[i][j] == 0:
        matrix[i]=[0]*n
        for j in matrix[i]:
            matrix[i][j]==0
    zero_positions=[(i,j)..]
for i,j in zero_positions:
    matrix[i]=[0]*n
    for i in range(rows):
        matrix[i][j]=0
    return matrix
"""
