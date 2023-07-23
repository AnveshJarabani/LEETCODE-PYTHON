def isSubsequence(self, s: str, t: str) -> bool:
    # s_list=list(s)
    # t_list=list(t)
    # for i in s_list:
    #     if t_list[0]==i:
    #         t_list.pop(0)
    # return not t_list
    for c in s:
        i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i + 1 :]
    return True
print(isSubsequence())
