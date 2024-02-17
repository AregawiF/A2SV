class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        left = 0
        for c in s:
            if c == "(":
                left += 1
                stack.append(c)
                val = True
            else:
                if val:
                    if stack:
                        stack.pop()
                        left -= 1
                        if left >0:
                            score += 2**left
                        else:
                            score += 1
                        val = False
                else:
                    stack.pop()
                    left -= 1
        return score