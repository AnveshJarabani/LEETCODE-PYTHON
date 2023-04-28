def mySqrt(x: int) -> int:
    if x==0 or x==1:
        return 0
    L,R=1,x//2
    while L<=R:
        mid=(L+R)//2
        if mid==x//mid:
            return mid
        elif mid<x//mid:
            L=mid+1
        else:
            R=mid-1
    return R
    
x=int(input())
print(mySqrt(x))