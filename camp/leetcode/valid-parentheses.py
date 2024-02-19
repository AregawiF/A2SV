class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {")":"(", "]":"[", "}":"{"}
        res = True
        for ch in s:
            if ch in chars.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif chars[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            res = False
        return res
                
                
        