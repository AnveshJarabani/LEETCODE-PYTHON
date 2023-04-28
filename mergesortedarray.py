import ast
def merge(L1,L2):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if len(L1)==1:
        if L1[0]==0:
            L1[0]=L2[0]
        else:
            L1
    else:
        ln=len(L1)
        for i in range(ln-1,-1,-1):
            if L1[i]!=0 or len(L2)==0:
                break
            L1[i]=L2[-1]
            L2.pop(-1)
        L1.sort()
        print(L1)
L1=ast.literal_eval(input())
L2=ast.literal_eval(input())
merge(L1,L2)