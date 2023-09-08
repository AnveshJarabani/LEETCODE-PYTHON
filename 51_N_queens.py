from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.']*n for _ in range(n)]
        col_set,diag_up,diag_down=set(),set(),set()
        def bt(row):
            if row==n:
                cpy=["".join(rw) for rw in board]
                print(cpy)
                res.append(cpy)
                return 
            print(board)
            for col in range(n):
                if col in col_set or row+col in diag_up or row-col in diag_down:
                    continue
                col_set.add(col)
                diag_up.add(row+col)
                diag_down.add(row-col)
                board[row][col]='Q'

                bt(row+1)
                
                col_set.remove(col)
                diag_up.remove(row+col)
                diag_down.remove(row-col)
                board[row][col]='.'
        bt(0)
        return res
print(Solution().solveNQueens(4))