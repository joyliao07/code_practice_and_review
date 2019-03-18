# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

class Solution:
    def myAtoi(self, str: str) -> int:
        answer = ''
        neg = False
        plus = False
        for what in str:
            if answer is '' and what is '-':
                if plus is False and neg is False:
                    neg = True
                else:
                    break
            elif answer is '' and what is '+':
                if neg is False and plus is False:
                    plus = True
                    what = ' '
                else:
                    break
            elif what.isdigit():
                answer += what
            elif what == ' ':
                if answer == '' and plus is False and neg is False:
                    pass
                else:
                    break
            else:
                break

        if answer == '':
            return(0)

        if answer != '':
            answer = int(answer)

            if neg is True:
                answer = answer * -1

            if answer > 2147483647:
                answer = 2147483647
            if answer < -2147483648:
                answer = -2147483648

        return answer
