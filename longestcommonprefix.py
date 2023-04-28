import ast

def longestCommonPrefix(List):
    List=sorted(List,key=len)
    result=""
    if len(List)==1 or len(List[0])==0:
        if List[0]:
            return List[0]
        else:
            return "\"\""
    for i, char in enumerate(zip(*List)):
        result=List[0][:i+1]
        if len(set(char))== 1:
            continue
        else:
            return List[0][:i]
    return result
x=ast.literal_eval(input())
print(longestCommonPrefix(x))
