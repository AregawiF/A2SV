class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_array = [0, nums[0]]
        for i in range(1, len(nums)):
            self.sum_array.append(self.sum_array[i] + nums[i])
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        result = self.sum_array[right+1] - self.sum_array[left] 
        return result
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)