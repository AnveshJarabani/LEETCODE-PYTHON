class Solution:
    def lls(self,s):
        l,res=0,0
        char_set=set()
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[i])
            res=max(res,i-l+1)
        return res
print(Solution().lls(input()))  
        