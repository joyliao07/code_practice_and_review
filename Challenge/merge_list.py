# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        current_3 = l3
        current_1 = l1
        current_2 = l2
        while current_1 and current_2:
            if current_2.val < current_1.val:
                current_3.next = current_2
                current_2 = current_2.next
                current_3 = current_3.next
            else:
                current_3.next = current_1
                current_1 = current_1.next
                current_3 = current_3.next
        while current_1:
            current_3.next = current_1
            current_1 = current_1.next
            current_3 = current_3.next
        while current_2:
            current_3.next = current_2
            current_2 = current_2.next
            current_3 = current_3.next
        return l3.next
