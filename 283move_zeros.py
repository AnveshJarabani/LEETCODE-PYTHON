import ast 
in_lst=ast.literal_eval(input())
def move_zeroes(in_lst):
    for i in in_lst:
        if i==0:
            in_lst.remove(0)
            in_lst.append(0)
    return in_lst


print(move_zeroes(in_lst))
