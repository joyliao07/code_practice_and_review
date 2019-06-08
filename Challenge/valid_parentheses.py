# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution:
    def isValid(self, s: str) -> bool:
        temp = ''

        for what in s:
            if what == '{' or what =='[' or what =='(':
                temp += what
            else:
                if what == '}':
                    what = '{'
                    if len(temp) == 0:
                        return False
                    elif temp[-1] == what:
                        temp = temp[:-1]
                    else:
                        return False
                elif what == ']':
                    what = '['
                    if len(temp) == 0:
                        return False
                    elif temp[-1] == what:
                        temp = temp[:-1]
                    else:
                        return False
                elif what == ')':
                    what = '('
                    if len(temp) == 0:
                        return False
                    elif temp[-1] == what:
                        temp = temp[:-1]
                    else:
                        return False

        if len(temp) != 0:
            return False

        return True
