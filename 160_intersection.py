
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a,b=headA,headB
        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
        return a


        # stack_a=[]
        # stack_b=[]
        # a,b=headA,headB
        # while a or b:
        #     if a in stack_b:
        #         return (f"intersected at {a.val}")
        #     else:
        #         stack_a.append(a)
        #     if b in stack_a:
        #         return (f"intersected at {b.val}")
        #     else:
        #         stack_b.append(b)
        # return "No intersection"
            
                