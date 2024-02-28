class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        s = str(num)
        nums = []
        res = ""
        if s[0] != "-":
            for c in s:
                nums.append(int(c))
            nums.sort()
            left = 0
            right = 0
            if nums[0] == 0:        
                while nums[right] == 0:
                    right += 1
                nums[0], nums[right] = nums[right], nums[0]
        else:
            for i in range(1,len(s)):
                nums.append(int(s[i]))
            nums.sort(reverse = True)
            left = 0
            right = 0
            if nums[0] == 0:       
                return 
            res += "-"
        for n in nums:
            res += str(n)
        
        return int(res)