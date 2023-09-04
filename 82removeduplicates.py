from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        l=dummy
        r=l.next
        while r:
            if r and r.next and r.val==r.next.val:
                while r.next and r.val==r.next.val:
                    r=r.next
                l.next=r.next
            else: l=l.next
            r=r.next
        return dummy.next
ar=[1,2,3,3,4,4,5]
cur_node=ListNode(ar[0])
head=cur_node
for i,val in enumerate(ar[1:]):
    node=ListNode(val)
    cur_node.next=node
    cur_node=node
x=Solution().deleteDuplicates(head)
while x:
    print(x.val)
    x=x.next
...
