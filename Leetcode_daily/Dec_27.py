class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        heap = []
        ans = 0
        curr = [0, 0]
        n = len(values)
        for i in range(n -2, -1, -1):
            val = values[i] - (n - i)
            heappush(heap, [-val, i])
        for j in range(n -1, -1, -1):
            if not heap:
                break
            currval, ind = heappop(heap)
            while heap and j <= ind:
                currval, ind = heappop(heap)
            if ind >= j:
                break
            score = values[j] + values[ind] + ind - j
            ans = max(ans, score)
            if not heap:
                break
            heappush(heap, [currval, ind])
        
        return ans