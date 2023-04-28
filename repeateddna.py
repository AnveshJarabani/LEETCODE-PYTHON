s=input()
class Solution:
    def repdna(self,s:str):
        hash={}
        for i in range(0,len(s)-9):
            sub=s[i:i+10]
            hash[sub]=hash.get(sub,0)+1
        return [i for i in hash.keys() if hash[i]>1]
        # lst=[s[i:i+10] for i in range(0,len(s)-9)]
        # return list(set([x for x in lst if lst.count(x)>1]))
        
print(Solution().repdna(s=s))