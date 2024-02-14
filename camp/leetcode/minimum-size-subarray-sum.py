class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        total = 0
        res = float('inf')
        for r in range(len(nums)):
            total = total + nums[r]
            while (total >= target):
                res = min(res, r-l+1)
                total = total - nums[l]
                l += 1
        if res == float('inf'):
            return 0
        else:
            return res

            


        