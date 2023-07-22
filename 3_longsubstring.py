""" 
This is a classic sliding window problem. 
When we need to find "longest" something, try to use sliding window. 
you start with no set and then keep updating the set as you traverse a given string/list
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp, result = 0, 0
        char_set = set()
        for rp in range(len(s)):
            while s[rp] in char_set:
                char_set.remove(s[lp])
                lp += 1
            char_set.add(s[rp])
            result = max(result, rp - lp + 1)
        return result
