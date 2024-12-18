class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [p for p in prices]
        stack = []
        for i, p in enumerate(prices):
            if not stack:
                stack.append((p, i))
            else:
                while stack and p <= stack[-1][0]:
                    curr, currind = stack.pop()
                    ans[currind] = prices[currind] - p
                stack.append((p, i))

        return ans