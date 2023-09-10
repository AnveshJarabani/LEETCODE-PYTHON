mod = 10**9 + 7


class Solution:
    memo = {}

    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        count = (self.countOrders(n - 1) * (2 * n - 1) * n) % mod
        self.memo[n] = count
        return count
