import functools
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.lru_cache(None)
        def defs(i,j):
            if i>=m or j>=n: return 0
            if i==m-1 and j == n-1: return 1
            return defs(i+1,j)+defs(i,j+1)
        return defs(0,0)
print(Solution().uniquePaths(3,7))