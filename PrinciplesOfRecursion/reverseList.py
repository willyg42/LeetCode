def reverseList(head):
    if not head or not head.next:
        return head
    ptr = reverseList(head.next)
    head.next.next = head
    head.next = None
    return ptr