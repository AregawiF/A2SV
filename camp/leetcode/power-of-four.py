class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return True if n == 1 else False if n < 1 else self.isPowerOfFour(n/4)