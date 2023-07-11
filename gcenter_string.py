def str_output(in_str):
    lst=[i for i in in_str]
    uniques=list(set(lst))
    uniques.sort()
    result_list=[[i,lst.count(i)] for i in uniques] #[[a,3],[b,3],[c,2]]
    result=""
    for i in result_list:
        result+=str(i[0])+str(i[1])
    return result

in_str="aabbbacc"
print(str_output(in_str))

