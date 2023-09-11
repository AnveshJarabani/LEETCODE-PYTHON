class Solution:
    def removeDuplicates(self, L) -> int:
        l=1
        for r in range(1,len(L)):
            if L[r]!=L[r-1]:
                L[l]=L[r]
                l+=1
        return l