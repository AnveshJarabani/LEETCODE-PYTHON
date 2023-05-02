def convert(s: str, n: int) -> str:
    if n==1: return s
    dct={r:"" for r in range(1,n+1)}
    r,up=1,True
    for i in s:
        dct[r]+=i
        if (r==1) or ((r<n) and up):
            r+=1
            up=True
        else:
            r-=1
            up=False
    return ''.join([dct[i] for i in dct.keys()])
print(convert(input(),int(input())))