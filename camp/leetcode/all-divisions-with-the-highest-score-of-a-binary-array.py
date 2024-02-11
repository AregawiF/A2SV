class Solution(object):
    def maxScoreIndices(self, nums):
        n = len(nums)
        prefix = [0] * (n+1)
        curr = 0
        for i in range(1,n+1):
            if nums[i-1] == 0:
                curr +=1
                prefix[i] = curr
            else:
                prefix[i] = curr
        suffix = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1]+nums[i]
        sum_arr = []
        for i in range(n+1):
            curr_sum = prefix[i] + suffix[i]
            sum_arr.append(curr_sum)
        max_sum = max(sum_arr)
        result = []
        for i in range(len(sum_arr)):
            if sum_arr[i] >= max_sum:
                result.append(i)
        return result
        