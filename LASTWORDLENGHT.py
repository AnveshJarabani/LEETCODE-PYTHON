import ast
input=input()
def lgt(input):
    result=0
    while input[-1]==" ":
        input=input[:-1]
    if input=="":
        return 0
    while input[-1]!=" ":
        result+=1
        input=input[:-1]
        if input=="":
            return result
    return result
print(lgt(input))
    
