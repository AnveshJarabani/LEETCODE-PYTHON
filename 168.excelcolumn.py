def convert(n):
    lst=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    res=''
    while n>0:
        res+=lst[(n-1)%26]
        n=(n-1)//26
    return res[::-1]
print(convert(int(input())))


   
    