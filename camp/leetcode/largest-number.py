class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums.sort(reverse = True)
        res = ""
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prev = str(nums[i]) + str(nums[j])
                curr = str(nums[j]) + str(nums[i])
                if int(curr) > int(prev):
                    nums[i], nums[j] = nums[j], nums[i]

        for n in nums:
            res += str(n)
        if int(res) == 0 :
            return "0"
        return res
