def title(cl):
    lst=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    res=0
    for i,n in enumerate(cl[::-1]):
        res+=(lst.index(n)+1)*26**(i)
    return res
print(title(input()))