# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        if num >= 1000:
            m_num = num // 1000
            roman += 'M' * m_num
            num -= 1000 * m_num
        if num >= 900:
            roman += 'CM'
            num -= 900
        if num >= 500:
            roman += 'D'
            num -= 500
        if num >= 400:
            roman += 'CD'
            num -= 400
        if num >= 100:
            c_num = num // 100
            roman += 'C' * c_num
            num -= 100 * c_num
        if num >= 90:
            roman += 'XC'
            num -= 90
        if num >= 50:
            roman += 'L'
            num -= 50
        if num >= 40:
            roman += 'XL'
            num -= 40
        if num >= 10:
            x_num = num // 10
            roman += 'X' * x_num
            num -= 10 * x_num
        if num >= 9:
            roman += 'IX'
            num -= 9
        if num >= 5:
            roman += 'V'
            num -= 5
        if num >= 4:
            roman += 'IV'
            num -= 4
        if num >= 1:
            i_num = num // 1
            roman += 'I' * i_num
            num -= i_num
        return roman
