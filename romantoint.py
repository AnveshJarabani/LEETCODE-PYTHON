my_dict={'I':1,
'V':5,
'X':10,
'L':50,
'C':100,
'D':500,
'M':1000,
'IV':4,'IX':9,
'XL':40,'XC':90,
'CD':400,'CM':900}
def romantoint(num) -> int:
    List=list(num)
    x=len(List)
    i=0
    while  i<len(List)-1:
        if List[i]+List[i+1] in my_dict.keys():
            List[i]=List[i]+List[i+1]
            List.pop(i+1)
        i+=1
    return sum(my_dict[v] for v in List)
x=input()
print(romantoint(x))