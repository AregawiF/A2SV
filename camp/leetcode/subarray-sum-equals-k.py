class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        my_dict = {0:1}
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        result = 0
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        for i in range(len(nums)):
            if (prefix[i] - k) in my_dict:
                result += my_dict[prefix[i] - k]
                if prefix[i] in my_dict:
                    my_dict[prefix[i]] += 1
                else:
                    my_dict[prefix[i]] = 1
            else:
                if prefix[i] in my_dict:
                    my_dict[prefix[i]] += 1
                else:
                    my_dict[prefix[i]] = 1
        return result