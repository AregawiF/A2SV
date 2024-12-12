class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        total = sum(gifts)
        heap = []
        for g in gifts:
            heappush(heap, -g)
        for _ in range(k):
            curr = -heappop(heap)
            temp = curr
            curr = math.floor(math.sqrt(curr))
            total -= (temp - curr)
            heappush(heap, -curr)
        return total