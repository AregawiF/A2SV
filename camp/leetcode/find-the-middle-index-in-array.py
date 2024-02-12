class Solution(object):
    def findMiddleIndex(self, nums):
        prefix = [nums[0]]
        suffix = [nums[-1]]
        result = 0
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])
        for i in range(len(nums)-2, -1 ,-1):
            suffix.insert(0,(suffix[0] + nums[i]))
        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                result = i
                break
            else:
                result = -1
        return result
        