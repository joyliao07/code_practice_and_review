# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    def romanToInt(self, s: str) -> int:
        if s == '':
            return 0
        num = 0
        lst = list(s)
        for i in range(len(lst)):
            if lst[i] == 'M':
                num += 1000
                lst[i] = ' '
            if len(lst) - i >= 2:
                if lst[i] == 'C' and lst[i+1] == 'M':
                    num += 900
                    lst[i] = ' '
                    lst[i+1] = ' '
            if lst[i] == 'D':
                num += 500
                lst[i] = ' '
            if len(lst) - i >= 2:
                if lst[i] == 'C' and lst[i+1] == 'D':
                    num += 400
                    lst[i] = ' '
                    lst[i+1] = ' '
            if lst[i] == 'C':
                num += 100
                lst[i] = ' '
            if len(lst) - i >= 2:
                if lst[i] == 'X' and lst[i+1] == 'C':
                    num += 90
                    lst[i] = ' '
                    lst[i+1] = ' '
            if lst[i] == 'L':
                num += 50
                lst[i] = ' '
            if len(lst) - i >= 2:
                if lst[i] == 'X' and lst[i+1] == 'L':
                    num += 40
                    lst[i] = ' '
                    lst[i+1] = ' '
            if lst[i] == 'X':
                num += 10
                lst[i] = ' '
            if len(lst) - i >= 2:
                if lst[i] == 'I' and lst[i+1] == 'X':
                    num += 9
                    lst[i] = ' '
                    lst[i+1] = ' '
            if lst[i] == 'V':
                num += 5
                lst[i] = ' '
            if len(lst) - i >= 2:
                if lst[i] == 'I' and lst[i+1] == 'V':
                    num += 4
                    lst[i] = ' '
                    lst[i+1] = ' '
            if lst[i] == 'I':
                num += 1
                lst[i] = ' '

        return num
