
def longpal(s):
    N=len(s)
    def lp(l,r):
        while l>=0 and r<N:
            if s[l]!=s[r]: break
            l-=1
            r+=1
        return l+1,r
    start,end=0,0
    for i in range(N):
        l,r=lp(i,i)
        if r-l>end-start:
            start=l
            end=r
        l,r=lp(i,i+1)
        if r-l>end-start:
            start=l
            end=r
    return s[start:end]






    # for i in range(0,len(s)):
    #     for j in range(1,len(s)+1):
    #         if s[i:j]==s[i:j][::-1] and long_pal<(j-i):
    #             long_pal=(j-i)
    #             res=s[i:j]
    # return res

print(longpal(input()))