class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        runsum = 0
        count = 0
        for cost in costs:
            runsum += cost
            if runsum <= coins:
                count += 1
            else:
                break
        return count


