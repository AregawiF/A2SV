class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= good - i:
                good = i

        if good == 0:
            return True
        else:
            return False

        