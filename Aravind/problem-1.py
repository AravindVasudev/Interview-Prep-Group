###############################################################################
# Given a linked list, rotate the list to the right by k places, where k is   #
# non-negative.                                                               #
# Example 1:                                                                  #
# Input: 1->2->3->4->5->NULL, k = 2                                           #
# Output: 4->5->1->2->3->NULL                                                 #
# Explanation:                                                                #
# rotate 1 steps to the right: 5->1->2->3->4->NULL                            #
# rotate 2 steps to the right: 4->5->1->2->3->NULL                            #
###############################################################################
import copy


class LinkedList:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
    def __len__(self):
        slow, fast = self, self
        length = 1
        while (slow.next is not None) and (fast is not None) and \
            (fast.next is not None):
                slow = slow.next
                fast = fast.next.next

                length += 2

        # Length is twice of midpoint distance. Remove 1 for even.
        return length - 1 if fast is None else length

    def __str__(self):
        serialized = str(self.data)
        ptr = self
        while ptr.next is not None:
            ptr = ptr.next
            serialized += ' -> ' + str(ptr.data)

        return serialized


def rotate_list_right(lst, k):
    """
    :param lst: A LinkedList
    :param k: A non-negative number of rotations
    """
    if (lst is None) or (k is 0):
        return lst

    length = len(lst)
    if k == length:
        return lst

    if k > length:
        k %= length

    ptr = lst
    for _ in range(length - k - 1):
        ptr = ptr.next

    last_node = ptr
    while last_node.next is not None:
        last_node = last_node.next

    last_node.next = lst
    new_head = ptr.next
    ptr.next = None

    return new_head


def main():
    """
    Test cases
    """
    # TODO: Clean up
    # Test Case 1
    test_case_1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
    output_1 = rotate_list_right(copy.deepcopy(test_case_1), 2)

    print('Input: ', test_case_1)
    print('Output: ', output_1)

    # Test Case 2
    test_case_2 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))
    output_2 = rotate_list_right(copy.deepcopy(test_case_2), 2)

    print('Input: ', test_case_2)
    print('Output: ', output_2)

    # Test Case 3
    test_case_3 = None
    output_3 = rotate_list_right(test_case_3, 2)

    print('Input: ', test_case_3)
    print('Output: ', output_3)

    # Test Case 4
    test_case_4 = LinkedList(1)
    output_4 = rotate_list_right(copy.deepcopy(test_case_4), 2)

    print('Input: ', test_case_4)
    print('Output: ', output_4)

    # Test Case 5
    test_case_5 = LinkedList(1, LinkedList(2))
    output_5 = rotate_list_right(copy.deepcopy(test_case_5), 2)

    print('Input: ', test_case_5)
    print('Output: ', output_5)

    # Test Case 6
    test_case_6 = LinkedList(1, LinkedList(2))
    output_6 = rotate_list_right(copy.deepcopy(test_case_6), 1)

    print('Input: ', test_case_6)
    print('Output: ', output_6)


if __name__ == '__main__':
    main()
