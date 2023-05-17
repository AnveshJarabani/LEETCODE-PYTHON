pattern=input()
s=input()
def word_pattern(pattern,s):
    s_lst=s.split(' ')
    stack_p={}
    stack_s={}
    if len(s_lst)!=len(pattern):
        return False
    for i,p in zip(s_lst,pattern):
        if p in stack_p and stack_p[p]!=i:
            return False
        if i in stack_s and stack_s[i]!=p:
            return False
        stack_p[p]=i
        stack_s[i]=p
    return True
print(word_pattern(pattern,s))
