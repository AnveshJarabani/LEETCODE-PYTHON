import ast
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def mergetwolists(x,y):
    if len(x)==0:
        return y
    elif len(y)==0:
        return x
    for position,i in enumerate(x):
        ListNode(val=i,next=x[position+1])



    return ListNode


x=ast.literal_eval(input())
y=ast.literal_eval(input())
print(mergetwolists(x,y))
