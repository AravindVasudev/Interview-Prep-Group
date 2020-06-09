def rotateRight(self, head: ListNode, k: int) -> ListNode:
    cursor, length = head, 0
    while cursor is not None:
        cursor = cursor.next
        length += 1 
    if length is 0:
        return head
    new_k = k%length
    if new_k is 0:
        return head
        
    dummy = ListNode(head)
    pre, ptr = dummy, head
    for i in range(length - new_k):
        pre, ptr = ptr, ptr.next
    pre.next, new_head = None, ptr
    while ptr is not None:
        pre, ptr = ptr, ptr.next
    pre.next = head
    return new_head
            
            
        