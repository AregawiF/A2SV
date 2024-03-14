class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        result = 0

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return result
