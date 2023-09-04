from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash_map={i:nums.count(i) for i in range(3)}
        j=0
        for i in range(len(nums)):
            while hash_map[j]==0:
                j+=1
            nums[i]=j
            hash_map[j]-=1

                
        return nums
print(Solution().sortColors(nums=[2,0,2,1,1,0]))