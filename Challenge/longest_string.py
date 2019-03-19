class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        acc = []
        for what in s:
            if what not in acc:
                acc.append(what)
        return len(acc)
