class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        right = 0
        window = {}
        ans = float('inf')
        while right < len(cards):
            if cards[right] not in window:
                window[cards[right]] = 1
            else:
                while cards[right] in window:
                    if cards[left] in window:
                        window.pop(cards[left])
                    left += 1
                window[cards[right]] = 1
                ans = min(ans, (right - left) + 2)
            right += 1

        if ans == float("inf"):
            return -1
        
        return ans
