# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        # testing if there is fast.next and move the markers down:
        while fast.next:
            fast = fast.next
            slow = slow.next

        # when it's at the end of the linked list:
        slow.next = slow.next.next

        return head
