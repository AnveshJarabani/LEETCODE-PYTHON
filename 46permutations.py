from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, callstack=[]):
            callstack.append(path)
            print(callstack)
            if not nums:
                result.append(path)
                callstack.pop()
                print(f"result={result}")
 
                print(callstack)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1 :], path + [nums[i]], callstack)

        result = []
        backtrack(nums, [])
        return result


print(Solution().permute([1, 2, 3]))
