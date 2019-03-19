# Exercise: Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0
        cur1, cur2 = l1, l2
        position = 1
        while cur1:
            num1 += (cur1.val * position)
            cur1 = cur1.next
            position *= 10

        position = 1
        while cur2:
            num2 += (cur2.val * position)
            cur2 = cur2.next
            position *= 10
        
        sum = num1 + num2
        
        lst = []
        position = 10
        while sum > 0:
            temp = sum % position
            sum -= temp
            lst.append(temp/(position/10))
            position *= 10
        if lst == []:
            return [0]
        else:
            return lst

############################################
####          TO PRINT SOLUTIONS:       ####
####                                    ####
############################################

# nums = [2, 7, 11, 15]
# target = 9
# solution = Solution()
# print(solution.twoSum(nums, target))
