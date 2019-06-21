# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Runtime 23%; Memory 95%"""
        if len(haystack) == 0:
            if len(needle) == 0:
                return 0  
            else:
                return -1

        length = len(needle)
        for i in range(len(haystack) + length):
            if haystack[i:(i+length)] == needle:
                return i
        return -1
        