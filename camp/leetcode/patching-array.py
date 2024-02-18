class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
            count = 0
            last = 0
            length = len(nums)
            i = 0
            while last < n:
                if i < length and nums[i] <= last+1:
                    last += nums[i]
                    i += 1
                else:
                    last += last+1
                    count += 1
            return count
