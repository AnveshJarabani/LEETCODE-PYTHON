
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_hash=[]
        cur=head
        while cur:
            node_hash.append(cur)
            cur=cur.next
            if cur in node_hash:
                return True
        return False

## TORTISE HARE METHOD --
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False