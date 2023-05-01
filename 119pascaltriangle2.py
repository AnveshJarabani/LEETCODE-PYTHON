# def generate(rn):
#     res = [[1]]
#     if rn == 0:
#         return res
#     for i in range(0, rn):
#         res.append(last_lst(res[-1]))
#     return res[-1]


# def last_lst(lst):
#     result = [lst[0]]
#     for i in range(0, len(lst)-1):
#         result.append(lst[i]+lst[i+1])
#     result.append(lst[-1])
#     return result
import ast

def generate(rn):
    output=[1]
    for i in range(1,rn+1):
        output.append(1)
        for j in range(len(output)-2,0,-1):
            output[j]+=output[j-1]
    return output
rn=ast.literal_eval(input())
print(generate(rn))