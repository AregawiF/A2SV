class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) -1 
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                if mid == len(nums)-1 or nums[mid+1] > target:
                    return mid + 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                if mid == 0 or  nums[mid-1] < target:
                    return mid 
                else:
                    right = mid - 1
            else:
                return mid