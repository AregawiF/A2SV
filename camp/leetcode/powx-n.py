class Solution:
    def myPow(self, x: float, n: int) -> float:
        def getpow(x,n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n < 0:
                return (1 / getpow(x, -n))
            else:

                half_pow = getpow(x, n // 2)
                if n % 2 == 0:
                    return half_pow * half_pow
                else:
                    return x * half_pow * half_pow 
        return getpow(x, n)