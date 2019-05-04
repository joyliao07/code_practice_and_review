# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lst = []
        res = []
        for num in digits:
            if num == "2":
                lst.append(['a', 'b', 'c'])
            elif num == "3":
                lst.append(['d', 'e', 'f'])
            elif num == "4":
                lst.append(['g', 'h', 'i'])
            elif num == "5":
                lst.append(['j', 'k', 'l'])
            elif num == "6":
                lst.append(['m', 'n', 'o'])
            elif num == "7":
                lst.append(['p', 'q', 'r', 's'])
            elif num == "8":
                lst.append(['t', 'u', 'v'])
            elif num == "9":
                lst.append(['w', 'x', 'y', 'z'])

        # lst = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
        for i in range(len(lst[0])):
          for j in range(len(lst[1])):
            for k in range(len(lst[2])):
              combo = lst[0][i]
              combo += lst[1][j]
              combo += lst[2][k]
              res.append(combo)
            
        return res



















