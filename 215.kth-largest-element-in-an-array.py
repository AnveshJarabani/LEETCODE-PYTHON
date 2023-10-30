from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        cur_nums = nums[:k]
        heapq.heapify(cur_nums)
        for i in nums[k:]:
            if i > cur_nums[0]:
                heapq.heappop(cur_nums)
                heapq.heappush(cur_nums, i)
        return cur_nums[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))
