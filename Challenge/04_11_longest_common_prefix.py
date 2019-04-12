# Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        length_lst = len(strs)
        first = strs[0]
        length_word = len(first)
        common = ''

        for i in range(length_word):
          counter = 0
          for a in range(1, length_lst):
            if len(strs[a]) < (i + 1):
              break
            else:
              if first[i] == strs[a][i]:
                counter += 1
              if counter == (length_lst - 1):
                common += first[i]
          if counter < (length_lst - 1):
            return common

        return(common)
