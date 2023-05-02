class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,res=0,0
        for i in nums:
            if count==0:
                res=i
            count+=(1 if i==res else -1)
        return res



# def maj(nums):
#     l=len(nums)
#     stack={}
#     if l==1: return nums[0]
#     for i in nums:
#         if i in stack.keys():
#             stack[i]+=1
#             if stack[i]>len(nums)/2:
#                 return i
#         else:
#             stack[i]=1
import ast            
print(maj(ast.literal_eval(input())))