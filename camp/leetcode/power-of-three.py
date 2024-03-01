class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        def power(num):
            if num == 1:
                return True
            elif num < 1:
                return False
            return power(num/3)

        return power(n)