# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Runtime 13.55%; Memory 72.72%"""
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

    def longestPalindrome_method_2(self, s: str) -> str:
        """Runtime 91.15%; Memory 33.26%"""
        longest = ''
        i = 0

        while i < len(s):
            l, r = i, i

            while r+1 < len(s) and s[r] == s[r+1]:
                r += 1
            i = r + 1

            ans = find_longest(s, l, r)

            if len(longest) < len(ans):
                longest = ans

        return longest

def find_longest(self, s, l, r):
    while (l >= 0 and r < len(s) and s[l] == s[r]):
        l -= 1
        r += 1
    return s[(l+1):r]












