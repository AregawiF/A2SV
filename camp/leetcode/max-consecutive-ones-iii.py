class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        longest = 0

        for r,num in enumerate(nums):
            if num == 0:
                k -= 1
            
            if k < 0:
                k += 1 - nums[l]

                l += 1

            else:
                longest = max(longest, r-l+1)

        return longest 
        