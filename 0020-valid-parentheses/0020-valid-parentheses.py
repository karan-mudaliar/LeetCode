class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'{':'}','(':')','[':']'}
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            elif len(stack) == 0 or dic[stack.pop()] != char:
                return False
        return not stack
             