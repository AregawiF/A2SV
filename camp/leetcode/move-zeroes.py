class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        if len(nums) < 2:
            return nums
        while nums[right] == 0 and left < right:
            right -= 1
        if right == left:
            return nums
        else:
            temp = nums[right]
            while left < len(nums) and left<right:
                while nums[left] == 0:
                    nums.insert(right+1, 0)
                    nums.remove(nums[left])
                    right -= 1
                left += 1
                
        return nums