# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        longest = ''
        for i in range(len(s)):
            phrase = ''
            for a in range(i, len(s)):
                phrase += s[a]
                if phrase == phrase[::-1]:
                    if length < len(phrase):
                        length = len(phrase)
                        longest = phrase

        return longest
