# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        """Runtime 90.57%; Memory 76.82%"""
        basket = []
        acc = ''
        self.generate(n, n, acc, basket)
        return basket

    def generate(self, left, right, acc, basket):
        if left > 0:
            self.generate(left - 1, right, acc + '(', basket)
        if right > 0 and right > left:
            self.generate(left, right - 1, acc + ')', basket)
        if left == 0 and right == 0:
            basket.append(acc)

