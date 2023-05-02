class Solution:
    def maxArea(self, lst: List[int]) -> int:
        n=len(lst)
        stack=[]
        for i in range(n-1):
            for j in range(i+1,n):
                stack.append(min(lst[j],lst[i])*(j-i))
        return max(stack)
    
# BIG O(N) - LINEAR TIME COMPLEXITY. 
# JUST MOVE ONE OF THE L OR R POINTERS BASED ON WHICH IS TALLER.
# THIS IS BECAUSE YOU WANT TO CHECK THE POSSIBILITY OF A BIGGER VALUE EXISTING. SO KEEP COMPARING WITH HIGHER VALS.
class Solution:
    def maxArea(self, lst: List[int]) -> int:
        n=len(lst)
        l,r=0,n-1
        max_vol=0
        while l<r:
            max_vol=max(max_vol,(r-l)*min(lst[l],lst[r]))
            if lst[l]<lst[r]:
                l+=1
            else: r-=1
        return max_vol