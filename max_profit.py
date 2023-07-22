"""
FIND THE LARGEST PROFIT POSSIBLE IN A LIST 

in cases like this, 
use two pointers, but the key is to move the lp to the current rp 
because we have already found the max from the past lp to current rp
so this makes the code efficient.

"""


class Solution:
    def maxProfit(self, lst: List[int]) -> int:
        lp, rp, max_profit = 0, 1, 0
        while rp < len(lst):
            if lst[lp] < lst[rp]:
                cur_profit = lst[rp] - lst[lp]
                max_profit = max(cur_profit, max_profit)
            else:
                lp = rp
            rp += 1
        return max_profit
