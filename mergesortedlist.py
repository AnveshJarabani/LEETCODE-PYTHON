import ast
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
L1=ast.literal_eval(input())
L2=ast.literal_eval(input())
def build_nodelist(L1):
    LN=ListNode(val=L1[0])
    CURNODE=LN
    for i in L1[1:]:
        NEW_NODE=ListNode(val=i)
        CURNODE.next=NEW_NODE
        CURNODE=NEW_NODE
    return LN
LN1=build_nodelist(L1)
LN2=build_nodelist(L2)
def combine_nodes(LN1,LN2):
    C1,C2=LN1,LN2
    if C1.val<C2.val:
        RES=ListNode(val=C1.val)
        CURNODE=RES
        C1=C1.next
    elif C1.val==C2.val:
        RES=ListNode(val=C1.val)
        CURNODE=RES
        CURNODE.next=ListNode(val=C1.val)
        C1=C1.next
        C2=C2.next
    else:
        RES=ListNode(val=C2.val)
        C2=C2.next
    while C1 and C2 is not None:
        if C1.val<C2.val:
            CURNODE.next=ListNode(val=C1.val)
            C1=C1.next
        elif C1.val==C2.val:
            CURNODE.next=ListNode(val=C1.val)

            CURNODE.next.next=ListNode(val=C1.val)
            C1=C1.next
            C2=C2.next
        else:
            CURNODE=ListNode(val=C2.val)
            C2=C2.next
    return RES
curnode=combine_nodes(LN1,LN2)
RES_List=[]
while curnode is not None:
    RES_List.append(curnode.val)
    curnode=curnode.next
print(RES_List)

