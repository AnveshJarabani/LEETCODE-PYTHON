my_dict= {'(': ')', '{': '}', '[':']'}
def isvalid(x):
    i=0
    if len(x)%2!=0:
        return False
    List=[i for i in x]
    while i<len(List)-1:
        if List[i] in my_dict.keys():
            if my_dict[List[i]]==List[i+1]:
                del List[i:i+2]
                i=0
                if len(List)==0:
                    return True
            else:
                i+=1
        else:
            i+=1
    return False
    #     if my_dict[x[i]]==x[i+1]:
    #         i+=2
    #         continue
    #     else:
    #         return False
    # return True
x=input()
print(isvalid(x))