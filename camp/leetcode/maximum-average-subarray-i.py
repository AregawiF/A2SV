class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k-1
        avgs = []
        currsum = sum(nums[left:right+1])
        avgs.append((currsum)/k)
        while right+1< len(nums):
            currsum -= nums[left]
            currsum += nums[right+1]
            avgs.append((currsum)/k)
            left += 1
            right += 1
        return max(avgs)

        