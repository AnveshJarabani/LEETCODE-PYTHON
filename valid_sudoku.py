"""
Sudoku Solver
Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable. If so, the function will returns true. Otherwise (i.e. there is no valid solution to the given sudoku board), returns false.

In sudoku, the objective is to fill a 9x9 board with digits so that each column, each row, and each of the nine 3x3 sub-boards that compose the board contains all of the digits from 1 to 9. The board setter provides a partially completed board, which for a well-posed board has a unique solution. As explained above, for this problem, it suffices to calculate whether a given sudoku board has a solution. No need to return the actual numbers that make up a solution.

A sudoku board is represented as a two-dimensional 9x9 array of the characters ‘1’,‘2’,…,‘9’ and the '.' character, which represents a blank space. The function should fill the blank spaces with characters such that the following rules apply:

In every row of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
In every column of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
In every 3x3 sub-board that is illustrated below, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with characters that abide to the constraints above. If the function succeeds in solving the sudoku board, it’ll return true (false, otherwise).

"""

from collections import defaultdict


def sudoku_solve(board):
    col = defaultdict(set)
    row = defaultdict(set)
    square = defaultdict(set)
    for i in range(9):
        for j in range(9):
            if (
                board[i][j] in row[i]
                or board[i][j] in col[j]
                or board[i][j] in square[(i // 3, j // 3)]
            ):
                return False
            row[i].add(board[i][j])
            col[j].add(board[i][j])
            square[(i // 3, j // 3)].add(board[i][j])
    return True


board = [
    [".", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["1", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]
print(sudoku_solve(board))
