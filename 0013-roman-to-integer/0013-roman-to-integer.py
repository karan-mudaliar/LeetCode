class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []
        maps = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        for char in s:
            value = maps[char]
            if stack and stack[-1] < value:
                stack[-1] = value - stack[-1]
            else:
                stack.append(value)
        return sum(stack)