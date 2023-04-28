import ast
in_list=ast.literal_eval(input())
def removeDuplicates(L):
    k=0
    if len(L)==0:
        return k
    else:
        counter=[]
        counter.append(L[0])
        while k<len(L)-1:
            if L[k]!=L[k+1]:
                counter.append(L[k+1])
            k+=1
    return counter
k=removeDuplicates(in_list)
print(k)