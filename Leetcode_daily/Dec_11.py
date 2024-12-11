class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 1
        left = 0
        for right in range(1, n):
            if nums[right] - nums[left] <= (2 * k):
                ans = max(ans, right - left + 1)
            else:
                while nums[right] - nums[left] > (2 * k):
                    left += 1

        return ans


