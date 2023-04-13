class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def initialize_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head


def is_list_equal(l1, l2):
    if not l1 and not l2:
        return True
    if not l1 or not l2:
        return False
    if l1.val != l2.val:
        return False
    return is_list_equal(l1.next, l2.next)


def reverseList(head):
    newHead, ptr = None, head
    while ptr:
        newNext = ptr.next
        ptr.next = newHead
        newHead = ptr
        ptr = newNext
    return newHead


if __name__ == '__main__':
    assert is_list_equal(reverseList(initialize_list([1,2,3,4,5])), initialize_list([5,4,3,2,1]))