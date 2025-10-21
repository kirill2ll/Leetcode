# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        result = True

        for ch in s:
            if ch in open:
                stack.append(ch)
            elif ch in close:
                if len(stack) == 0:
                    result = False
                    break
                element_to_compare = stack.pop()
                if open.index(element_to_compare) != close.index(ch):
                    result = False
                    break
        
        if len(stack) > 0:
            result = False

        return result

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("]"))