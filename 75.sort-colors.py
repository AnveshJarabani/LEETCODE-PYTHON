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


"""
can you keep pushing the zeros back until it's a zero?
and then keep pushing ones until it's a 1?
same goes with 2s? leaves twos in position cuz if it's a one or zero only then we will keep pushing them backwards. 
so then user only one pointer? 
for i in range(len(nums)):
    if nums[i] ==0:
        continue
    elif nums[i] ==2:
        nums[i+1]=nums[i]
        
"""


