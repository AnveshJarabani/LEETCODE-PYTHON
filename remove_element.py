import ast
lst=ast.literal_eval(input())
val=ast.literal_eval(input())
def remove_val(lst,val):
    result=[]
    for i in lst:
        if i!=val:
            result.append(i)
    return result
result=remove_val(lst,val)
print(result)