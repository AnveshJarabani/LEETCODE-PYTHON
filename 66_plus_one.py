
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = str(int("".join([str(i) for i in digits])) + 1)
        return [int(i) for i in num]


print(Solution().plusOne(digits=[1, 2, 3]))
