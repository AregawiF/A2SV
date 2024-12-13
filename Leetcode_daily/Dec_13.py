class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        n = len(nums)
        indices = [(nums[i], i) for i in range(n)]
        indices.sort()
        score = 0
        for i in range(n):
            ind = indices[i][1]
            if ind not in marked:
                score += indices[i][0]
                marked.add(ind)
                marked.add(ind -1)
                marked.add(ind +1)
        return score        