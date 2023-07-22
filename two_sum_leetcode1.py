# use hashmap when the problem statement has 'unique solution' available mentioned


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for indx, val in enumerate(nums):
            if target - val in hash_map:
                return [hash_map[target - val], indx]
            else:
                hash_map[val] = indx
