import ast 
in_lst=ast.literal_eval(input())
def move_zeroes(in_lst):
    # for i in in_lst:
    #     if i==0:
    #         in_lst.remove(0)
    #         in_lst.append(0)
    # return in_lst
    l=0
    for r in range(len(in_lst)):
        if in_lst[r]:
            in_lst[l],in_lst[r]=in_lst[r],in_lst[l]
            l+=1
print(move_zeroes(in_lst))
