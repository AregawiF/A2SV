class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for a in arr:
            if stack and a < stack[-1]:
                old_max = stack[-1]
                while stack and a < stack[-1]: 
                    stack.pop()
                stack.append(old_max)
            else:
                stack.append(a)

        return len(stack)