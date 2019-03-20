# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y == y[::-1]:
            return True
        else:
            return False
