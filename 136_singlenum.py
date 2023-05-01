import ast
def single(nums):
    res=0
    for n in nums:
        res= n^res
    return res
    
    
    # stack=[]
    # for i in nums:
    #     if i in stack:
    #         stack.remove(i)
    #     else:
    #         stack.append(i)
    # return stack[0]
    
print(single(ast.literal_eval(input())))

