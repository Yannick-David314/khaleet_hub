class Solution:
    def isValid(self, s: str) -> bool:
        ref = {')':'(', ']':'[','}':'{'}
        stack = []

        for char in s:
            if char in ref:
                if not stack:
                    return False
                temp = stack.pop()
                if ref[char] != temp:
                    return False
            else:
                stack.append(char)
        return not stack
        