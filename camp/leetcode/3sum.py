class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # left = 0
        ans = []
        for third in range(len(nums)):
            if third > 0 and nums[third] == nums[third - 1]:
                continue
            left = third + 1
            right = len(nums) - 1
            while left < right:
                if nums[third] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[third] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    ans.append([nums[third], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                   
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
