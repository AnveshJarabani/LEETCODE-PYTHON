class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set = set()
        diag_up, diag_dn = set(), set()
        res = 0

        def bt(row):
            if row == n:
                nonlocal res
                res += 1
                return
            for col in range(n):
                if col in col_set or (row - col) in diag_up or (row + col) in diag_dn:
                    continue
                col_set.add(col)
                diag_up.add(row - col)
                diag_dn.add(row + col)
                bt(row + 1)
                col_set.remove(col)
                diag_up.remove(row - col)
                diag_dn.remove(row + col)

        bt(0)
        return res


print(Solution().totalNQueens(4))
