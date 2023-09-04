class Solution:
    def trap(self, ht: List[int]) -> int:
        l, r = 0, len(ht) - 1
        l_max, r_max, res = ht[l], ht[r], 0
        while l < r:
            if ht[l] < ht[r]:
                l += 1
                l_max = max(ht[l], l_max)
                res += l_max - ht[l]
            else:
                r -= 1
                r_max = max(ht[r], r_max)
                res += r_max - ht[r]
        return res
