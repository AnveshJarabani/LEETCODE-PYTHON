class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result_list = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == start:
                    result_list.append(str(start))
                else:
                    result_list.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        if start == nums[-1]:
            result_list.append(str(start))
        else:
            result_list.append(f"{start}->{nums[-1]}")
        return result_list
