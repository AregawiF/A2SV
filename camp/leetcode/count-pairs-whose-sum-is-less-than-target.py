class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = 1
        ans = 0
        while (right< len(nums)) and (left < right) :
            while right < len(nums) and (nums[left] + nums[right]) < target:
                ans += 1
                right += 1
            left += 1
            right = left + 1
        return ans

        