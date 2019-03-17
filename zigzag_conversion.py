# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        lst = []

        for i in range(numRows):
            lst.append([])

        position = 0
        spe = False

        for what in s:
            if spe is False:
                position += 1
            if spe is True:
                position -= 1

            if position > numRows and spe is False:
                position = (numRows - 1)
                spe = True

            if position == 1 and spe is True:
                position = 1
                spe = False

            lst[(position - 1)].append(what)

        output = ''
        for i in range(numRows):
            for a in range(len(lst[i])):
                output += lst[i][a]

        return output
