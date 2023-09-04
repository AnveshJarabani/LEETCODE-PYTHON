class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        span1,span2,span3=len(s1),len(s2),len(s3)
        if (span1+span2)!=span3: return False
        p1,p2,p3=0,0,0
        while p1<span1 and p2<span2 and p3<span3:
            if s1[p1]==s3[p3]:
                p1+=1
                p3+=1
            elif s2[p2]==s3[p3]:
                p2+=1
                p3+=1
            else:
                return False
        return s3[p3:]==s1[p1:]+s2[p2:]
print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))