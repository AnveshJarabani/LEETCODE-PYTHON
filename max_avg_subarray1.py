class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        result = sum(nums[:k])
        max_sum = result
        for i in range(k, len(nums)):
            result += nums[i] - nums[i - k]
            max_sum = max(max_sum, result)
        return max_sum / k


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
