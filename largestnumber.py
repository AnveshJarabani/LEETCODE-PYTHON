import ast
from functools import cmp_to_key
lst=ast.literal_eval(input())
class Solution:
    def largestNumber(self, nums) -> str:
        nums=[str(i) for i in nums]
        def comp(a,b):
            if a+b<b+a:
                return 1
            else:
                return -1
        lst=sorted(nums,key=cmp_to_key(comp))
        return str(int(''.join(str(i) for i in lst)))
print(Solution().largestNumber(nums=lst))