class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednums = sorted(nums)
        ans = []
        mydict = {}
        for i in range(len(nums)-1, -1, -1):
            temp = i
            if i > 0:
                while sortednums[i-1] == sortednums[i]:
                    if i == 0:
                        break
                    i -= 1
                mydict[sortednums[temp]] = i
            else:
                mydict[sortednums[temp]] = 0
        for n in nums:
            ans.append(mydict[n])
        return ans