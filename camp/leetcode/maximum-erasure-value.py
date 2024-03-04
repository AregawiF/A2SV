class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        currsum = 0
        ans = 0
        window = set()
        while right < len(nums):
            if nums[right] not in window:
                window.add(nums[right])
                currsum += nums[right]
                ans = max(ans, currsum)
            else:
                while nums[right] in window:
                    window.remove(nums[left])
                    currsum -= nums[left]
                    left += 1
                window.add(nums[right])
                currsum += nums[right]
                ans = max(ans, currsum)

            right += 1
        return ans

