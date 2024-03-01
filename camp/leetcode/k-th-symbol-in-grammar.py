class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        left = 0
        right = 2 ** (n-1)
        for _ in range(n-1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid
                if curr == 0:
                    curr = 1
                else:
                    curr = 0
        return curr