"""
FIND THE LARGEST PROFIT POSSIBLE IN A LIST 

in cases like this, 
use two pointers, but the key is to move the lp to the current rp 
because we have already found the max from the past lp to current rp
so this makes the code efficient.

"""
from typing import List
x=[1,2,3]
for i,val in enumerate(x):
    x.pop(i)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp, total_profit = 0, 1, 0
        while rp < len(prices):
            if prices[rp] > prices[lp]:
                total_profit += prices[rp] - prices[lp]
                lp = rp
            else:
                lp = rp
            rp += 1
        return total_profit
