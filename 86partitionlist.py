from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        cur_node=dummy.next
        less_head=None
        more_head=None
        while cur_node.next:
            if cur_node.val<x:
                if not less_head:
                    less_head=ListNode(val=cur_node.val)
                    les_cur=less_head
                    continue
                les_cur.next=ListNode(val=cur_node.val)
                les_cur=les_cur.next
            else:
                if not more_head:
                    more_head=ListNode(val=cur_node.val)
                    more_cur=more_head
                    continue
                more_cur.next=ListNode(val=cur_node.val)
                more_cur=more_cur.next
            cur_node=cur_node.next
        les_cur.next=more_head
        return less_head

lst = [1,4,3,2,5,2]
x = 3
head=ListNode(val=lst[0])
cur_node=head
for i in lst[1:]:
    cur_node.next=ListNode(i)
    cur_node=cur_node.next
Solution().partition(head,x)