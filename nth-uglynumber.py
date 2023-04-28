n=int(input())
class Solution:
    def isUgly(self, n: int) -> bool:
        count=1
        val=1
        result=1
        while count<n+1:
            val=result
            for i in [2,3,5]:
                while val%i==0:
                    val//=i
            if val==1:
                 count+=1
                 result+=1
            else:
                result+=1
        return result-1
print(Solution().isUgly(n=n))