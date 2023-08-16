from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hash_map={n:nums.count(n) for n in nums}
        def df():
            if len(temp)==len(nums):
                result.append(temp.copy())
                return
            for n in hash_map:
                if hash_map[n]>0:
                    temp.append(n)
                    hash_map[n]-=1
                    df()
                    hash_map[n]+=1
                    temp.pop()
        result,temp=[],[]
        df()
        return result
print(Solution().permuteUnique([1,1,3]))