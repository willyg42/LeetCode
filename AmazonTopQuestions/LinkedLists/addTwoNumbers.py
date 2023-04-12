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


def addTwoNumbers(l1, l2):
    total = 0
    l3 = ListNode()
    head = l3
    carry = 0
    while l1 or l2:
        l1val = l1.val if l1 else 0
        l2val = l2.val if l2 else 0
        total = l1val + l2val + carry
        l3.next = ListNode(total % 10)
        carry = total // 10
        l3 = l3.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry > 0:
        l3.next = ListNode(carry)
    return head.next


if __name__ == '__main__':
    l1 = initialize_list([2,4,3])
    l2 = initialize_list([5,6,4])
    assert is_list_equal(addTwoNumbers(l1, l2), initialize_list([7,0,8]))
    l1 = initialize_list([9,9,9,9,9,9,9])
    l2 = initialize_list([9,9,9,9])
    assert is_list_equal(addTwoNumbers(l1, l2), initialize_list([8,9,9,9,0,0,0,1]))