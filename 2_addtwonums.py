class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s_1,s_2=self.get_str(l1),self.get_str(l2)
        res=str(int(s_1)+int(s_2))[::-1]
        return build_listnode([i for i in res])
    def get_str(self,l):
        if not l:
            return ""
        return self.get_str(l.next)+str(l.val)
import ast
l1=ast.literal_eval(input())
l2=ast.literal_eval(input())
def build_listnode(l1):
    root=ListNode(l1[0])
    cur=root
    for i in l1[1:]:
        node=ListNode(i)
        cur.next=node
        cur=node
    return root
r1=build_listnode(l1)
r2=build_listnode(l2)

Solution().addTwoNumbers(r1,r2)