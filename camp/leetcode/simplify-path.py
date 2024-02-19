class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for p in path:
            if p == "..":
                if not stack:
                    continue
                else:
                    stack.pop()
            elif p == "." or p == '':
                continue
            else:
                stack.append(p)
        return "/"+"/".join(stack)