class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        if len(s) == 1:
            if s[0] in vowels:
                return 1
            else:return 0
        
        left = 0
        right = 0
        ans = 0
        count = 0
        while right < len(s):
            while right < (k - 1):
                if s[right] in vowels:
                    count += 1
                right += 1
            if s[right] in vowels:
                count += 1
            ans = max(count, ans)
            if s[left] in vowels:
                count -= 1
            left += 1
            right += 1

        return ans