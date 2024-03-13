# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

        # left = 0
        # right = n
        # if n == 1:
        #     return 1
        # while left <= right:
        #     mid = (left + right)//2
        #     if left == right -1 or left == right:
        #         if isBadVersion(left):
        #             return left + 1
        #         else:
        #             return right + 1 
        #     if isBadVersion(mid):
        #         right = mid 
        #     elif isBadVersion(mid) == False:
        #         left = mid + 1     

