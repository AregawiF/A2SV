class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mydict = {0:1}
        count = 0
        curr = 0
        
        for num in nums:
            curr += num
            diff = curr - goal
            count += mydict.get(diff, 0)
            mydict[curr] = mydict.get(curr,0) + 1

        return count