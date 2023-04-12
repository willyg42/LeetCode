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


def mergeTwoLists(list1, list2):
    list3 = ListNode()
    head = list3
    while list1 or list2:
        l1val = list1.val if list1 else float('inf')
        l2val = list2.val if list2 else float('inf')
        if l1val <= l2val:
            list3.next = ListNode(l1val)
            list1 = list1.next
        else:
            list3.next = ListNode(l2val)
            list2 = list2.next
        list3 = list3.next
    return head.next


if __name__ == '__main__':
    l1 = initialize_list([1,2,4])
    l2 = initialize_list([1,3,4])
    assert is_list_equal(mergeTwoLists(l1, l2), initialize_list([1,1,2,3,4,4]))