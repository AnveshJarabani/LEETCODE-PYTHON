from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(i=0,path=[]):
            if i>=len(nums):
                res.append(path[:])
                return
            path.append(nums[i])
            bt(i+1,path)
            path.pop()
            bt(i+1,path)
        bt()
        return res
    
print(Solution().subsets(nums=[1,2,3]))