from typing import List
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         s=[]
#         p1,p2=0,0
#         while p1<len(nums1) and p2<len(nums2):
#             if nums1[p1]<nums2[p2]:
#                 s.append(nums1[p1])
#                 p1+=1
#             else:
#                 s.append(nums2[p2])
#                 p2+=1
#         if p1==len(nums1):
#             s.extend(nums2[p2:])
#         else:
#             s.extend(nums1[p1:])
#         n=len(s)-1
#         if (n + 1)% 2 == 0:
#             return (s[n//2]+s[(n//2)+1])/2
#         else:
#             return s[n//2]
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def popper(nums1,nums2):
            if nums1 and nums2:
                if nums1[0]<nums2[0]:
                    val=nums1.pop(0)
                else:
                    val=nums2.pop(0)
            elif nums1:
                val=nums1.pop(0)
            elif nums2:
                val=nums2.pop(0)
            return val,nums1,nums2
        s=[]
        n=len(nums1)+len(nums2)-1
        if (n+1)%2==0:
            even=True
        else:
            even=False
        cur=n
        while nums1 or nums2:
            cur-=1
            val,nums1,nums2=popper(nums1,nums2)
            if cur==n//2:
                if not even:
                    val2,nums1,nums2=popper(nums1,nums2)
                    return val2
                else:
                    val2,nums1,nums2=popper(nums1,nums2)
                    return (val+val2)/2

nums1 = []
nums2 = [1]     
print(Solution().findMedianSortedArrays(nums1,nums2))