# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """Runtime 95.03%; Memory 70.15%"""
        p = 0
        if head is None:
            return
        if head.next is None:
            return head
        current = head
        c_next = head.next
        temp = True
        previous = None
        while c_next:
            if previous:
                previous.next = c_next
            current.next = c_next.next
            c_next.next = current
            if temp == True:
                temp_head = c_next
                temp = False
            previous = current
            current = current.next
            if current:
                c_next = current.next
            else:
                break

        return temp_head
























