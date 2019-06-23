# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """Runtime 74.83%; Memory 99.86%"""
        answer = dividend // divisor
        
        if answer < (-2**31):
            return (-2**31)
        elif answer > (2**31 -1):
            return (2**31 -1)
        elif answer < 0 and answer != dividend/divisor:
            return(answer +1)
        else:
            return answer
