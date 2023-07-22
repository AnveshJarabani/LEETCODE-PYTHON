class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return True
            i += 1
        return False


import ast

print(Solution().containsDuplicate(ast.literal_eval(input())))
