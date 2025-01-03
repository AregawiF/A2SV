class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        suffix = [0] * (n + 1)
        for i in range(n -1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]


        ans = 0
        for i in range(n -1):
            if prefix[i] >= suffix[i + 1]:
                ans += 1
        return ans