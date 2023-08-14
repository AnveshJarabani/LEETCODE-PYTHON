from typing import Optional
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        holder=ListNode(0,next=head)
        left=holder
        right=head
        while n>0 and right:
            right=right.next
            n-=1
        while right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return holder.next