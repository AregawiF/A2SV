class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = 2
        ans = []
        for third in range(len(nums)):
            left = third + 1
            right = len(nums) - 1
            while left < right:
                if nums[third] + nums[left] + nums[right] > target:
                    ans.append(nums[third] + nums[left] + nums[right])
                    right -= 1
                elif nums[third] + nums[left] + nums[right] < target:
                    ans.append(nums[third] + nums[left] + nums[right])
                    left += 1
                else:
                    return target
        res = float("inf")
        result = 0
        for a in ans:
            if abs(a - target) < res:
                res = abs(a - target)
                result = a
        return result

        # while left < right and right < len(nums):

        #     currsum = nums[left] + nums[left+1] + nums[right]
            
        # return ans
