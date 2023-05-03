def swapPairs(head):
    if not head or not head.next:
        return head
    firstNode = head
    secondNode = head.next
    firstNode.next = swapPairs(secondNode.next)
    secondNode.next = firstNode
    return secondNode