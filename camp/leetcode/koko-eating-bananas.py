import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(rate):
            hours = 0
            for bananas in piles:
                if bananas <= rate:
                    hours += 1
                else:
                    hours += math.ceil(bananas / rate)
            return hours

        low, high = 1, max(piles)
        while low <= high:
            mid = low + (high - low)//2
            if checker(mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low