def reverseList(head):
    if not head:
        return None
    newhead=head
    if head:
        newHead=reverseList(head)
        head.next.next=head
    head.next=None
    return newhead
    