class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        mod = 10 ** 9 + 7
        @cache
        def dp(curr):
            temp = 0
            if curr >= low and curr <= high:
                temp += 1
            if curr > high:
                return temp

            return (temp + dp(curr + zero) + dp(curr + one)) % mod 
        
        return dp(0) % mod