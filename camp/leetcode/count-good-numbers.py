class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def power(x, y):
            result = 1
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % mod
                y //= 2
                x = (x * x) % mod
            return result

        count = 1
        count *= power(5, (n + 1) // 2)
        count *= power(4, n // 2)

        return count % mod

