class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        chars = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            chars[s[right]] = 1 + chars.get(s[right], 0)

            while ((right - left + 1) - max(chars.values())) > k:
                chars[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans