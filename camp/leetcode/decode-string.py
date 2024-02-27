class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                chars = ""
                while stack[-1] != "[":
                    chars =  stack.pop() + chars
                
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(chars * int(num) )
        return "".join(stack) 
