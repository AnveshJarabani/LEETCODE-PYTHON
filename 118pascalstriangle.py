import ast


# def generate(rn):
#     res = [[1]]
#     if rn == 1:
#         return res
#     for i in range(1, rn):
#         res.append(last_lst(res[-1]))
#     return res


# def last_lst(lst):
#     result = [lst[0]]
#     for i in range(0, len(lst)-1):
#         result.append(lst[i]+lst[i+1])
#     result.append(lst[-1])
#     return result
def generate(rn):
    res=[]
    for i in range(rn):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=res[i-1][j-1]+res[i-1][j]
        res.append(row)
    return res

num = ast.literal_eval(input())
print(generate(num))


