class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, curr, count):
            if i == len(nums):
                if curr == target:
                    count += 1
                return count

            
            return dp(i+1, curr + nums[i], count) + dp(i+1, curr - nums[i], count)

        return dp(0, 0, 0)