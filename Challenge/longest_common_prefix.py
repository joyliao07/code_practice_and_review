# Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0 or strs[0] == '':
            return ''
            
        common = strs[0]

        match = True
        letter_index = 0
        shared = ''

        while match == True and letter_index <= (len(common) - 1):
            
            for i in range(1, len(strs)):
                if strs[i] == '':
                    return ''
                    break
                if common[letter_index] == strs[i][letter_index]:
                    if i == (len(strs) - 1):
                        shared += common[letter_index]
                    else:
                        pass
                else:
                    match = False
            
            letter_index += 1

        return shared
