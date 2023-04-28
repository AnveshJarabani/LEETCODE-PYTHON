import ast
digits=ast.literal_eval(input())
def plusone(digits):
    if len(digits)==0:
        return [1]
    val=""
    for i in digits:
        val+=str(i)
    result=str(int(val)+1)
    return [int(i) for i in result]
print(plusone(digits))