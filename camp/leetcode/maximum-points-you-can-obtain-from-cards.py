class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k
        currsum = sum(cardPoints[right:])
        ans = currsum
        while right < len(cardPoints):
            currsum += (cardPoints[left] - cardPoints[right])
            ans = max(ans, currsum)
            left += 1
            right += 1

        return ans